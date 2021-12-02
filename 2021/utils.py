from functools import wraps
import time


def timed(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        begin = time.time()
        result = f(*args, **kwargs)
        delta = time.time() - begin
        print('Executed {} in {} sec'.format(f.__name__, delta))
        return result
    return wrapper
