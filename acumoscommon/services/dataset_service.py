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
