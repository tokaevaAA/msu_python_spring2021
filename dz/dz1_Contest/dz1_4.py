def get_amt_digits(x):
    otv = 0
    while(x != 0):
        otv = otv + 1
        x = x // 10
    return otv


N, K = map(int, input().split())
tek = N
otv = 0
for i in range(1, K + 1):
    otv = otv + tek
    tek = 10 ** get_amt_digits(N) * tek + N
print(otv)
