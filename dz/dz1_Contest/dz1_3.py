a = float(input())
a_rub = int(a)
a_kop = int((a - a_rub) * 100)

nominals_rub = [10, 5, 2, 1]
nominals_kop = [50, 10, 5, 1]
amt_rub = []
amt_kop = []

for i in range(len(nominals_rub)):
    amt_rub.append(a_rub // nominals_rub[i])
    a_rub = a_rub % nominals_rub[i]
for i in range(len(nominals_kop)):
    amt_kop.append(a_kop // nominals_kop[i])
    a_kop = a_kop % nominals_kop[i]

for i in range(len(nominals_rub)):
    if (amt_rub[i] != 0):
        print("{:5.2f}\t{} ".format(float(nominals_rub[i]), amt_rub[i]))
for i in range(len(nominals_kop)):
    if (amt_kop[i] != 0):
        print("{:5.2f}\t{} ".format(float(nominals_kop[i] / 100), amt_kop[i]))
