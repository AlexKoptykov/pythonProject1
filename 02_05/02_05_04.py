t = input()
if t[-2::] == 'ой' or t[-2::] == 'ый' or t[-2::] == 'ий':
    print('Мужской')
else:
    if t[-2::] == 'ая' or t[-2::] == 'яя':
        print('Женский')
    else:
        print('Средний')