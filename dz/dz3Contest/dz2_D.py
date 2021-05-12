import functools


def counter(func):
    def reset():
        wrapper.rdepth = 0
        wrapper.ncalls = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal tek_depth

        if tek_depth == 0:
            reset()

        tek_depth += 1
        wrapper.ncalls += 1
        wrapper.rdepth = max(wrapper.rdepth, tek_depth)

        try:
            return func(*args, **kwargs)
        finally:
            tek_depth -= 1

    tek_depth = 0
    reset()
    return wrapper
