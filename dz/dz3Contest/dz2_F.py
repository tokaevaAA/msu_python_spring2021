def expand_seq(n, openb, closeb, s):
    if (openb + closeb < 2 * n):
        if openb < n:
            Str = s + "("
            yield from expand_seq(n, openb + 1, closeb, Str)
        if closeb < openb:
            Str = s + ")"
            yield from expand_seq(n, openb, closeb + 1, Str)
    else:
        yield s


def brackets(n):
    s = ""
    yield from expand_seq(n, 0, 0, s)


if __name__ == "__main__":
    n = int(input())
    for i in brackets(n):
        print(i)
