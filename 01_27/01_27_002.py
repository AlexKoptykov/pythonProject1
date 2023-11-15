k = int(input('Сколько строк? '))
flag = False
for i in range(k):
    line = input()
    f = len(line)
    if i > 0 and f % p == 0:
        flag = True
    p = f
print('Ура!' if flag else 'Увы!')