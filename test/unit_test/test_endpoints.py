#!/usr/bin/env python3
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

import json
from flask import Flask
from unittest.mock import patch
from test.unit_test.mock_context import memcache_test_context
from acumoscommon.services.model_manager_service import ModelManagerService


app = Flask(__name__)

with memcache_test_context():
    from microservice_flask import initialize_app
    initialize_app(app)


def test_get_algorithms():
    with app.test_client() as c:
        response = c.get('/v2/algorithms')
    assert response.status_code == 200
    data = json.loads(response.get_data())
    assert len(data) > 1


def test_get_status_404():
    with app.test_client() as c:
        response = c.get('/v2/builders/not_found_key/status')
    assert response.status_code == 404


@patch.object(ModelManagerService, 'upload_model')
def test_get_create(upload_model):

    body = {
        'algorithm': 'gbm',
        'trainingDatasetKey': 'h2o',
        'validationDatasetKey': 'h2o',
        'y': 'species',
        'x': ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    }

    request_headers = {
        'content-type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Basic password',
    }

    with app.test_client() as c:
        response = c.post('/v2/builders', data=json.dumps(body), headers=request_headers)
    assert response.status_code == 202
    assert "Accepted" in json.loads(response.get_data())['message']

    response_data = json.loads(response.get_data())
    mem_cache_key = response_data['key']

    with app.test_client() as c:
        response = c.get(f'/v2/builders/{mem_cache_key}/status')
    assert response.status_code == 200

    with app.test_client() as c:
        response = c.post(f'/v2/builders/{mem_cache_key}/exporter')
    assert response.status_code == 201
