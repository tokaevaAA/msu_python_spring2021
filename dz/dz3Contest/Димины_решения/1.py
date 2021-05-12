def counter(func):
    def reset():
        wrapper.rdepth = 0
        wrapper.ncalls = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        if not hasattr(wrapper,'ncalls'):
            setattr(wrapper, 'ncalls', 0)

        if not hasattr(wrapper,'tek_depth'):
            setattr(wrapper, 'tek_depth', 0)

        if wrapper.tek_depth == 0:
            reset()
        wrapper.tek_depth+=1
        wrapper.rdepth=max(wrapper.rdepth,wrapper.tek_depth)
        result=func(*args, **kwargs)
        wrapper.tek_depth-=1

        wrapper.ncalls+=1

        #print(max_depth)
        return result
    return wrapper

@counter
def func2(n, steps):
    if steps == 0:
        return
    func2(n + 1, steps - 1)
    func2(n - 1, steps - 1)

func2(0,5)
print(func2.ncalls, func2.rdepth)
func2(0,3)
print(func2.ncalls, func2.rdepth)
