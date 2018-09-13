# -*- coding: utf-8 -*-
# ===============LICENSE_START=======================================================
# Acumos Apache-2.0
# ===================================================================================
# Copyright (C) 2017-2018 AT&T Intellectual Property & Tech Mahindra. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END=========================================================
import pytest
import json
from microservice_flask import app, initialize_app

BASE_URL = 'http://127.0.0.1:8061/v2/'


@pytest.fixture(scope='session')
def test_client():
    
    testing_client = app.test_client()
    initialize_app(testing_client)
    testing_client.testing = True
    return testing_client


# @api.route('/status/<string:statusKey>')
def test_get_status(test_client):
    response = test_client.get(BASE_URL + 'status/' + 'dummyStatusKey')
    assert response.status_code == 400
    assert json.loads(response.get_data())['message'] == 'TODO: This API is just a stub. Method not yet implemented'

# @api.route('/asyncPredictions')
def test_get_asyncPredictions(test_client):

    body = {
        'readDatasetKey': 'm09286_1530026027076_855258959068650452',
        'writeDatasetKey': 'm09286_1530026122667_683407214566211287'
    }

    request_headers = {
        'content-type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Basic password',
        'codecloud-authorization': 'Basic password',
        'ATT-ModelVersion': '1.0',
        'ATT-ModelKey': 'com-att-cmlp_m09286_ST_CMLPPLGRD_pmmlModelIris',
        'ATT-MessageId': 'rh1832_callback_id1',
        'ATT-ReturnURL': 'http://localhost:8123/v2/callback'
    }

    response = test_client.post(BASE_URL + 'asyncPredictions', data=json.dumps(body), headers=request_headers)
    assert response.status_code == 400
    assert json.loads(response.get_data())['message'] == 'TODO: This API is just a stub. Method not yet implemented'


# @api.route('/syncPredictions')
def test_get_syncPredictions(test_client):

    body = '''
        Id,Sepal_Length,Sepal_Width,Petal_Length,Petal_Width
        record-001,7.0,3.2,4.7,1.4
        record-002,7.0,3.0,5.0,1.0
        record-003,6.0,3.2,4.7,1.4
        '''

    request_headers = {
        'content-type': 'text/csv',
        'accept': 'text/csv',
        'Authorization': 'Basic password',
        'codecloud-authorization': 'Basic password',
        'ATT-ModelVersion': '1.0',
        'ATT-ModelKey': 'com-att-cmlp_rh1832_ST_CMLPPLGRD_pmmlModelIris'
    }

    response = test_client.post(BASE_URL + 'syncPredictions', data=body, headers=request_headers)
    assert response.status_code == 400
    assert json.loads(response.get_data())['message'] == 'TODO: This API is just a stub. Method not yet implemented'
