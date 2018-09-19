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
