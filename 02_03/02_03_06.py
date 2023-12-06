t = input()
while t != 'Стоп':
    t1 = len(t[-1])
    t = input()
    if t1 == len(t[-1]):
        r = 'НЕВЕРНО'
    else:
        r = 'ВЕРНО'
print(r)