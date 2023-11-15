s = input('?')
flag = 'ХОРОШЕЕ'
while s != '':
    if 'кровь' in s or\
        'любовь' in s:
        flag = 'НЕ ХОРОШЕЕ'
    s = input('?')
print(flag)