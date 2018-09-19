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
from contextlib import contextmanager
from unittest.mock import patch
import json
from os.path import dirname, realpath, join


class MockedMockCacheObject():

    def __init__(self):
        self.cache = []

    def Client(self, host, port):
        return self

    def set(self, key, value):
        self.cache.append([key,  value])

    def get(self, key):
        for item in self.cache:
            if item[0] == key:
                json_obj = json.loads(item[1])
                if 'path' not in json_obj:
                    model_file = join(dirname(realpath(__file__)), 'dummyFile')
                    with open(model_file, 'w+') as file:
                        file.write("This is a test")

                    json_obj['path'] = model_file
                    json_obj = json.dumps(json_obj)
                return json_obj.encode()
        return None


@contextmanager
def memcache_test_context():
    """Custom test context for mocking out Memcache"""

    with patch('pymemcache.client.base', new=MockedMockCacheObject()):
        yield
