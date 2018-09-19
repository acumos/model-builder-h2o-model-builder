from acumoscommon.config_util import get_config_value, get_properties_path
from acumoscommon.responses import not_found, accepted_response
from acumoscommon.service_utils import get_dataset_contents
from acumoscommon.services.model_manager_service import ModelManagerService
from acumoscommon.tasks.task_pool import get_task_pool
from flask import request

from h2o.estimators.naive_bayes import H2ONaiveBayesEstimator
from h2o.estimators.gbm import H2OGradientBoostingEstimator
from pymemcache.client import base
import h2o
import json
import logging
import os
import tempfile
import uuid
import io


logger = logging.getLogger(__name__)

TRAINING_FILE = "training"


def _get_memcached_client():
    # TODO (pk9069): make this configurable
    return base.Client(('localhost', 11211))


# TODO (pk9069): move to enum
class MLAlgorithm():
    NAIVE_BAYES = "naivebayes"
    GRADIENT_BOOSTING_MACHINE = "gbm"


def get_algorithms():
    algo_path = os.path.join(get_properties_path(), 'algorithms.json')
    with open(algo_path) as f:
        return json.loads(f.read())


# TODO (pk9069): move to external class
def _run_builder(key, algorithm, training_dataset_key, y, x):
    try:
        client = _get_memcached_client()
        contents = get_dataset_contents(training_dataset_key)
        with tempfile.TemporaryDirectory() as tmpdir:
            dataset_path = os.path.join(tmpdir, TRAINING_FILE)
            with open(dataset_path, 'w') as training_file:
                training_file.write(contents)
            h2o.init()
            training_frame = h2o.import_file(dataset_path)

            if algorithm == MLAlgorithm.NAIVE_BAYES:
                # naivebayes expects the prediction response to be categorical
                training_frame[y] = training_frame[y].asfactor()
                estimator = H2ONaiveBayesEstimator()
            elif algorithm == MLAlgorithm.GRADIENT_BOOSTING_MACHINE:
                estimator = H2OGradientBoostingEstimator()

            kwargs = {
                'training_frame': training_frame,
                'y': y
            }
            if x is not None:
                kwargs['x'] = x

            estimator.train(**kwargs)
            path = h2o.save_model(model=estimator, path='/tmp')
            model_performance = estimator.model_performance()
            details = {
                'mse': model_performance.mse()
            }

            client.set(key, json.dumps({
                'status': 'COMPLETE',
                'description': 'Model has been built',
                'details': details,
                'path': path
            }))
    except Exception as ex:
        client.set(key, json.dumps({'status': 'FAILED', 'description': str(ex)}))
        logger.exception("Building model failed")


def create_builder():
    obj = request.get_json()

    training_dataset_key = obj.get('trainingDatasetKey')
    algorithm = obj.get('algorithm')
    y = obj.get('y')
    x = obj.get('x', None)

    key = str(uuid.uuid4())
    client = _get_memcached_client()
    client.set(key, json.dumps({'status': 'INPROGRESS', 'description': 'Model is currently being built'}))
    task_pool = get_task_pool()
    args = (key, algorithm, training_dataset_key, y, x)
    task_pool.apply_async(_run_builder, args)
    return accepted_response('Accepted', f'/v2/builders/{key}/status', additional_values={'key': key})


def get_builder_status(key):
    client = _get_memcached_client()
    status = client.get(key)
    if status is None:
        not_found(f'{key} not found.')
    status_object = json.loads(status.decode())
    # TODO (pk9069): clean this piece up later
    del status_object['path']
    return status_object


def export_model(key):
    client = _get_memcached_client()
    status = client.get(key)
    if status is None:
        not_found(f'{key} not found.')
    status_object = json.loads(status.decode())
    path = status_object['path']

    section = 'SERVICES'
    model_manager_endpoint = get_config_value('modelmanager_service', section=section)

    # TODO configure these
    catalog = {
        "name": key,
        "modelType": "Classification",
        "modelFormat": "H2O",
        "projectKey": "ACUMOS",
        "icon": "",
        "description": "",
        "sharedUsers": [],
        "sharedRoles": [],
        "subscribedUsers": [],
        "isSharedAll": True,
        "modelComment": "",
        "documentComment": "",
        "metadata": [],
        "customMetadata": []
    }

    catalog_file = io.StringIO(json.dumps(catalog))
    model_manager_service = ModelManagerService(model_manager_endpoint, binary=True, verify_ssl=False)

    with open(path, 'rb') as model_file:
        model_manager_service.upload_model(model_file, catalog_file)

    return catalog, 201
