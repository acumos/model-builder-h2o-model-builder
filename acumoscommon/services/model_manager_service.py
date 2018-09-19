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
from logging import getLogger
from tempfile import NamedTemporaryFile

import requests
import os


logger = getLogger(__name__)

API_VERSION = 'v2'
MODELS_RESOURCE = 'models'
CONTENTS_RESOURCE = 'contents'


class ModelManagerException(Exception):
    def __init__(self, body, status_code, message=None):
        self.body = body
        self.status_code = status_code

        if message is None:
            message = 'ModelManagerException: Status code: {}. Response Body: {}'.format(
                status_code, body)
        super(ModelManagerException, self).__init__(message)


class ModelManagerService:

    def __init__(self, endpoint, binary=False, verify_ssl=True):
        self._endpoint = endpoint
        self.headers = {}
        self.binary = binary
        self.verify_ssl = verify_ssl


    # Takes file objects as input
    def upload_model(self, model, catalog, document=None):
        endpoint = self._endpoint + '/' + API_VERSION + '/' + MODELS_RESOURCE

        logger.debug('Sending request endpoint {}'.format(endpoint))

        files = {
            'file': model,
            'catalog': catalog
        }
        if document is not None:
            files['document'] = document

        response = requests.post(endpoint, files=files, headers=self.headers, verify=self.verify_ssl)

        if response.status_code != 201:
            raise ModelManagerException(response.text, response.status_code)
        return response.json()
