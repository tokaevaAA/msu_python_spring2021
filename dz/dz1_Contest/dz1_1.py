n = int(input())
mas = list(map(int, input().split()))
myset = set()
for i in range(n):
    if (mas[i] not in myset):
        print(mas[i], end=' ')
    myset.add(mas[i])

print('')
print(n - len(myset))
