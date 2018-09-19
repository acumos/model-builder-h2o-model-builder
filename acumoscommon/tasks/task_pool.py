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
import signal

from multiprocessing import Pool
from acumoscommon.config_util import get_config_value


# Depending on how the WSGI server is being ran, there may be multiple task pools.
# For example, if the server starts 2 processes, each process will have its own task pool.
_task_pool = None


def initializer():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def get_task_pool():
    global _task_pool
    if _task_pool is None:
        pool_size = int(get_config_value('task_pool_size', section='TASK_POOL'))
        _task_pool = Pool(processes=pool_size, initializer=initializer)
    return _task_pool
