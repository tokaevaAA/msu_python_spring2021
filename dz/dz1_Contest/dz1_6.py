import collections
mas1 = list(map(str, input().split()))
mas2 = list(map(str, input().split()))
for i in range(len(mas1)):
    mas1[i] = mas1[i].lower()
for i in range(len(mas2)):
    mas2[i] = mas2[i].lower()

otv = 1
mydict1 = collections.defaultdict(int, dict(collections.Counter(mas1)))
mydict2 = collections.defaultdict(int, dict(collections.Counter(mas2)))
for k in set(mydict1.keys()).union(set(mydict2.keys())):
    if (mydict1[k] < mydict2[k]):
        otv = 0
        break
if (otv == 1):
    print("YES")
else:
    print("NO")
