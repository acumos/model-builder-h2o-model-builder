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
from acumoscommon.responses import not_found
from acumoscommon.services.datasource_service import DatasourceService
from acumoscommon.services.dataset_service import DatasetService
from acumoscommon.config_util import get_config_value
import logging
import json
import time
import requests


def status_callback(callback_url, correlation_id, authorization_header, status, status_description):
    headers = {
        'Authorization': authorization_header,
        'Content-Type': 'application/json',
        'ATT-MessageId': correlation_id
    }
    body = {
        'status': status,
        'status_description': status_description
    }

    logging.debug('Sending POST request to %s', callback_url)
    call_success = False

    try:
        response = requests.post(callback_url, data=json.dumps(body), headers=headers)
        if (response.status_code != 204 or response.status_code != 200):
            call_success = True
    except Exception as ex:
        logging.exception(f'First try at callback failed for callback url {callback_url}')
        logging.exception(str(ex))

    counter = 1
    num_retries = int(get_config_value('num_retries_callback', section="CALLBACK"))
    sleep_time = int(get_config_value('wait_between_retries', section="CALLBACK"))

    while not call_success and counter < num_retries:
        time.sleep(sleep_time)
        counter += 1
        try:
            response = requests.post(callback_url, data=json.dumps(body), headers=headers)

            if (response.status_code != 204 or response.status_code != 200):
                call_success = True
        except Exception as ex:
            logging.exception(f'Retry attempt {counter} failed for the callback url: {callback_url}')
            logging.exception(str(ex))

    if call_success:
        logging.debug('Status code: {}'.format(response.status_code))
        logging.debug('Response text: {}'.format(response.text))
        return response
    else:
        return None


def write_back_scoring(write_dataset_key, scoring, dataset_endpoint=None, dataource_endpoint=None):

    logging.debug(f'Writing back datasource information from dataset using key {write_dataset_key}')
    if not dataset_endpoint:
        dataset_endpoint = get_config_value(env_name='dataset_service', section='SERVICES')
    dataset_service = DatasetService(dataset_endpoint,)

    if not dataource_endpoint:
        dataource_endpoint = get_config_value(env_name='datasource_service', section='SERVICES')
    datasource_service = DatasourceService(dataource_endpoint)

    # Get the dataset details which contains the datasource key
    dataset_details = dataset_service.get_dataset_details(write_dataset_key)

    obj = json.loads(dataset_details)
    write_datasource_key = obj.get("datasourceKey")
    logging.debug(f'Found write back source key {write_datasource_key} using dataset key {write_dataset_key}')

    datasource_details = datasource_service.get_datasource_details(write_datasource_key)
    obj = json.loads(datasource_details)

    if type(obj) is list and len(obj) > 0:
        writeback_catagory = obj[0].get("category")
        logging.debug(f'Found write back category to be of type {writeback_catagory}')
    else:
        not_found(f'Write back datasource key {write_datasource_key} not found')

    write_back_unformatted(write_datasource_key, scoring, dataource_endpoint)


def write_back_unformatted(write_datasource_key, scoring, dataource_endpoint=None):

        logging.debug(f'Writing back datasource information using key {write_datasource_key}')

        if not dataource_endpoint:
            dataource_endpoint = get_config_value(env_name='datasource_service', section='SERVICES')

        datasource_service = DatasourceService(dataource_endpoint)
        datasource_service.post_write_content(write_datasource_key, scoring)

        logging.debug(f'Successfully wrote back datasource contents for {write_datasource_key}')


def get_dataset_contents(read_dataset_key, dataset_endpoint=None, dataource_endpoint=None):

        logging.debug(f'Get datasource information from dataset using key {read_dataset_key}')
        if not dataset_endpoint:
            dataset_endpoint = get_config_value(env_name='dataset_service', section='SERVICES')
        dataset_service = DatasetService(dataset_endpoint)

        if not dataource_endpoint:
            dataource_endpoint = get_config_value(env_name='datasource_service', section='SERVICES')
        datasource_service = DatasourceService(dataource_endpoint)

        # Get the dataset details which contains the datasource key
        dataset_details = dataset_service.get_dataset_details(read_dataset_key)

        obj = json.loads(dataset_details)
        read_datasource_key = obj.get("datasourceKey")

        datasource_contents = datasource_service.get_datasource_contents(read_datasource_key)

        return datasource_contents
