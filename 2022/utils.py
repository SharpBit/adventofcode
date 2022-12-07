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


def read_lines(fname: str) -> list:
    with open(f'inputs/{fname}') as f:
        return [line.rstrip() for line in f.readlines()]

def read_split(fname: str, sep: str) -> list:
    with open(f'inputs/{fname}') as f:
        return [line.rstrip() for line in f.read().split(sep)]

def read_file(fname: str) -> str:
    with open(f'inputs/{fname}') as f:
        return f.read().rstrip()
