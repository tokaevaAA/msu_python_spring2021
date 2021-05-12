def sew(mas1, mas2):
    if len(mas1) == 0:
        return mas2
    if len(mas2) == 0:
        return mas1
    if mas1[0] > mas2[0]:
        mas1, mas2 = mas2, mas1
    otv = []
    otv.append(mas1[0])
    i = 1
    j = 0
    while (i < len(mas1) and j < len(mas2)):
        while (j < len(mas2) and mas2[j] < mas1[i]):
            otv.append(mas2[j])
            j = j + 1
        otv.append(mas1[i])
        i = i + 1
    while (i < len(mas1)):
        otv.append(mas1[i])
        i = i + 1
    while(j < len(mas2)):
        otv.append(mas2[j])
        j = j + 1
    return otv


def merge_sort(mas, group_len=1):
    mas = [el for el in mas]
    if (group_len >= len(mas)):
        return
    new_mas = []
    i = 0
    while (i + 2 * group_len - 1 <= len(mas)):
        mas1 = mas[i: i + group_len]
        mas2 = mas[i + group_len: i + 2 * group_len]
        for el in sew(mas1, mas2):
            new_mas.append(el)
        i = i + 2 * group_len
    if (i + group_len - 1 <= len(mas)):
        mas1 = mas[i: i + group_len]
        mas2 = mas[i + group_len:]
        for el in sew(mas1, mas2):
            new_mas.append(el)
    else:
        for el in mas[i: ]:
            new_mas.append(el)
    yield new_mas
    yield from merge_sort(new_mas, 2 * group_len)
