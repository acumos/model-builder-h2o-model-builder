#
# ===============LICENSE_START=======================================================
# Acumos
# ===================================================================================
# Copyright (C) 2018 AT&T Intellectual Property. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END=========================================================
import pytest
import json
from os.path import dirname, realpath, join
import sys
parentddir = dirname(dirname(dirname(realpath(__file__))))
sys.path.append(join(parentddir, 'modelbuilder'))

from modelbuilder.app import app, initialize_app

BASE_URL = 'http://127.0.0.1:8061/v2/'


@pytest.fixture(scope='session')
def test_client():
    testing_client = app.test_client()
    initialize_app(testing_client)
    testing_client.testing = True
    return testing_client


# @api.route('/algorithms')
def test_get_algorithms(test_client):
    response = test_client.get(BASE_URL + 'algorithms')
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'


# @api.route('/builders')
def test_post_builders(test_client):

    body = {
        'algorithm': 'gbm',
        'trainingDatasetKey': 'm09286_1530026122667_683407214566211287',
        'validationDatasetKey': 'm09286_1530026122667_683407214566211286',
        'y': 'species',
        'x': ['petal_length', 'petal_width', 'sepal_length', 'septal_width']
    }

    request_headers = {
        'content-type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Basic password',
    }

    response = test_client.post(BASE_URL + 'builders', data=json.dumps(body), headers=request_headers)
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'


# @api.route('/builders/<string:key>/status')
def test_get__builders_status(test_client):
    response = test_client.get(BASE_URL + 'builders/dummy_key/status')
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'


# @api.route('/builders/<string:key>/exporter')
def test_post_builders_exporter(test_client):

    request_headers = {
        'content-type': 'application/json',
        'accept': 'text/csv',
        'Authorization': 'Basic password',
    }

    response = test_client.post(BASE_URL + 'builders/dummy_key/exporter', headers=request_headers)
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'
