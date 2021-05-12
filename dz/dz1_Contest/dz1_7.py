import sys


def safe_input():
    try:
        return input()
    except EOFError:
        sys.exit(0)


def one_round(start, stop):
    step = (stop - start) // 10
    for i in range(10):
        if (i == 9 and stop == 100001):
            print('?', start + (i + 1) * step - 1) # their stupid rule that questions <=100000
        else:
            print('?', start + (i + 1) * step)
    print("+")
    has1 = 0
    for i in range(10):
        tek_answer = int(safe_input())
        if (tek_answer == 1 and has1 == 0):
            otv = tuple([start + i * step, start + (i + 1) * step])
            has1 = 1
    if (has1 == 0):
        otv = tuple([100001 - step, 100001])
    return otv


start = 1 #included
stop = 100001 #excluded
for i in range(5):
    start1, stop1 = one_round(start, stop)
    start = start1
    stop = stop1
print('!', start)
