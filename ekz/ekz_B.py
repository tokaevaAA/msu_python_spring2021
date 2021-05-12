import time
import functools
import math


def retry(check, n_attempts=5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **argv):
            nonlocal n_attempts
            state_of_check = False
            if (n_attempts is None or n_attempts <= 0):
                while True:
                    result = func(*args, **argv)
                    state_of_check = check(result)
                    if (state_of_check):
                        break
            else:
                for i in range(n_attempts):
                    result = func(*args, **argv)
                    state_of_check = check(result)
                    if (state_of_check):
                        break
            if (state_of_check is False):
                raise RuntimeError("Expired number of retries")
            return result
        return wrapper
    return decorator
