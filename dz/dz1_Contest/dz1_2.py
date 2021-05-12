def get_sum_of_digits(x):
    otv = 0
    tek = x
    while (tek != 0):
        otv += tek % 10
        tek = tek // 10
    return tuple([otv, x])


n = int(input())
mas = list(map(int, input().split()))
otv = sorted(mas, key=get_sum_of_digits)
for i in range(n):
    print(otv[i], end=' ')
