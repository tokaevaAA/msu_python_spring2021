import re
from functools import reduce
import operator


def solution1(mas):
    return list(map(lambda x: int(re.sub(r'[,-.]', '', x).strip()[-1::-1]), mas))


def solution2(mas):
    return list(map(lambda x: x[0] * x[1], mas))


def solution3(mas):
    return list(filter(lambda x: x % 6 in [0, 2, 5], mas))


def solution4(mas):
    return list(filter(lambda x: bool(x), mas))


def solution5(mas):
    list(map(lambda x: operator.setitem(x, 'square', x['width'] * x['length']), mas))
    return mas


def solution6(mas):
    return list(map(lambda x: dict(**x, square=x['width'] * x['length']), mas))


def solution7(mas):
    return set(reduce(lambda x, y: x.intersection(y), mas))


def solution8(mas):
    return dict(reduce(lambda x, y: (operator.setitem(x, y, x[y] + 1) or x), mas, {i: 0 for i in set(mas)}))


def solution9(mas):
    return list(map(lambda x: x['name'], list(filter(lambda x: x['gpa'] > 4.5, mas))))


def solution10(mas):
    return list(filter(lambda x: reduce(
                                        lambda x, y: int(x) + int(y),
                                        x[::2]) == reduce(lambda x, y: int(x) + int(y), x[1::2]), mas))


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
