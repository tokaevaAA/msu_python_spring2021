from time import sleep
import functools
import signal


class TimeoutException(Exception):
    def __init__(self, message):
        super(TimeoutException, self).__init__(message)


def signal_handler(signum, frame):
    raise TimeoutException("Timed out")


def timeout(seconds=None):
    def decorator(func):
        if (seconds is None or seconds < 0):
            return func

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if (seconds is not None and seconds > 0):
                signal.signal(signal.SIGALRM, signal_handler)
                signal.setitimer(signal.ITIMER_REAL, seconds)
            result = 0
            try:
                result = func(*args, **kwargs)
            finally:
                signal.setitimer(signal.ITIMER_REAL, 0)
                signal.signal(signal.SIGALRM, signal.SIG_DFL)
            return result
        return wrapper
    return decorator
