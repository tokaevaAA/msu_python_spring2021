def chain_loop(args):
    iter_list = [iter(i) for i in args]
    ind = 0
    while (len(iter_list) > 0):
        if (ind >= len(iter_list)):
            ind = 0
        try:
            x = next(iter_list[ind])
            yield x
            ind += 1
        except StopIteration:
            iter_list.pop(ind)
