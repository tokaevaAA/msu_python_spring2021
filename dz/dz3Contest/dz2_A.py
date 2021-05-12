def solution1(mas):
    return [x*4 for x in mas]


def solution2(mas):
    return [x * (i + 1) for (i, x) in enumerate(mas)]


def solution3(mas):
    return [i for i in range(16) if (i % 5 == 0 or i % 3 == 0)]


def solution4(mas):
    return [el for m in mas for el in m]


def solution5(n):
    return [(i, j, k)
            for i in range(1, n + 1)
            for j in range(1, n + 1)
            for k in range(1, n + 1)
            if (i ** 2 + j ** 2 == k ** 2 and i <= j <= k)]


def solution6(mas):
    return [list(i + j for j in mas[1]) for i in mas[0]]


def solution7(mas):
    return [list(m[j] for m in mas) for (j, _) in enumerate(mas[0])]


def solution8(mas):
    return [list(int(x) for x in m.split()) for m in mas]


def solution9(mas):
    return {chr(ord('a') + x): x ** 2 for x in mas}


def solution10(mas):
    return {x[0].upper() + x[1:].lower() for x in mas if len(x) > 3}


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
