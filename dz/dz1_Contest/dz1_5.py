n = int(input())
data = []
for i in range(n):
    data.append(str(input()))

otv = []
for i, name in enumerate(data):
    mas_of_letters = sorted(list(name))
    string_of_letters = str()
    for el in mas_of_letters:
        string_of_letters = string_of_letters + str(el)
    otv.append(tuple([string_of_letters, i]))

otv = sorted(otv)

prev_str = otv[0][0]
for i in range(len(otv)):
    tek_str = otv[i][0]
    tek_word = data[otv[i][1]]
    if (tek_str != prev_str):
        print('')
    print(tek_word, end=' ')
    prev_str = tek_str
