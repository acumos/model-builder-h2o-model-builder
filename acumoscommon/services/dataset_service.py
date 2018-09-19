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
import requests
from logging import getLogger

logger = getLogger(__name__)


API_VERSION = 'v2'
CONTENTS_RESOURCE = 'datasets'


class DatasetServiceException(Exception):
    def __init__(self, body, status_code, message=None):
        self.body = body
        self.status_code = status_code

        if message is None:
            message = f'DatasetServiceException: Status code: {status_code}. Response Body: {body}'
        super().__init__(message)


class DatasetService:
    def __init__(self, endpoint, verify_ssl=True):
        self.endpoint = endpoint
        self.headers = {

        }
        self.verify_ssl = verify_ssl

    def get_dataset_details(self, dataset_key):
        endpoint = f'{self.endpoint}/{API_VERSION}/{CONTENTS_RESOURCE}/{dataset_key}'
        response = requests.get(endpoint, headers=self.headers, verify=self.verify_ssl)
        logger.debug('Status code: {}'.format(response.status_code))
        if response.status_code != 200:
            text = response.text
            raise DatasetServiceException(text, response.status_code)
        return response.text
