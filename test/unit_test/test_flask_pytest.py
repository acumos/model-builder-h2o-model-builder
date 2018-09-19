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
import pytest
import json
import os
import platform
from os.path import dirname, realpath, join
import sys
import subprocess
from pymemcache.client import base

from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread


parentddir = dirname(dirname(dirname(realpath(__file__))))
sys.path.append(join(parentddir, 'modelbuilder'))

from modelbuilder.app import app, initialize_app

BASE_URL = 'http://127.0.0.1:8061/v2/'


@pytest.fixture(scope='session', autouse=True)
def test_client(request):
    testing_client = app.test_client()
    initialize_app(testing_client)
    testing_client.testing = True

    # Test model file
    model_filename = join(join(parentddir, 'test'), 'h2o_model')

    # Setup test case uploading model
    with open(model_filename, 'w+') as model_file:
        model_file.write("This is a test")


    # Setup test case for getting model builder status
    cmd = ['memcached', '-d', 'start']
    mem_proc = subprocess.Popen(cmd, shell=True)
    mem_client = base.Client(('localhost', 11211))
    mem_client.set('test_key', json.dumps({
        'status': 'COMPLETE',
        'description': 'Model has been built',
        'details': "This is just a test",
        'path': model_filename
    }))


    # Setup mocked model manager
    mock_server = HTTPServer(('localhost', 8063), MockServerRequestHandler)

    # Start running mock server in a separate thread.
    # Daemon threads automatically shut down when the main process exits.
    mock_server_thread = Thread(target=mock_server.serve_forever)
    mock_server_thread.setDaemon(True)
    mock_server_thread.start()

    # Set model manager to mocked port
    os.environ['modelmanager_service'] = 'http://localhost:8063'


    # TODO Validate on *nix system
    def tear_down():
        if platform.system() == 'Windows':
            os.system("taskkill /f /im memcached.exe")
        else:
            mem_proc.kill()
    
    request.addfinalizer(tear_down)

    return testing_client


# @api.route('/algorithms')
def test_get_algorithms(test_client):
    response = test_client.get(BASE_URL + 'algorithms')
    assert response.status_code == 200
    data = json.loads(response.get_data())
    assert len(data) > 1


# @api.route('/builders')
def test_post_builders(test_client):

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

    response = test_client.post(BASE_URL + 'builders', data=json.dumps(body), headers=request_headers)
    assert response.status_code == 202
    assert "Accepted" in json.loads(response.get_data())['message']








# @api.route('/builders/<string:key>/status')
def test_get__builders_status(test_client):
    response = test_client.get(BASE_URL + 'builders/test_key/status')
    assert response.status_code == 200
    assert json.loads(response.get_data())['status'] == 'COMPLETE'


# @api.route('/builders/<string:key>/exporter')
def test_post_builders_exporter(test_client):

    request_headers = {
        'content-type': 'application/json',
        'accept': 'text/csv',
        'Authorization': 'Basic password',
    }

    response = test_client.post(BASE_URL + 'builders/test_key/exporter', headers=request_headers)
    assert response.status_code == 201
    assert json.loads(response.get_data())['name'] == 'test_key'


class MockServerRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):

        # If this is for model manager
        if '/v2/models' in self.requestline:
            # TODO GET FULL RESPONSE
            response_json = {
                "key": "test_key",
                "name": "h2o_model",
            }
            json_string = json.dumps(response_json)

            self.send_response(201, response_json)
            self.end_headers()
            self.wfile.write(bytes(json_string, "utf-8"))

        else:
            self.send_response(200, "Dummy Success")
        self.end_headers()
        return
