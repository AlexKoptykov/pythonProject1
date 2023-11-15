xa = int(input('Введите координату x для А '))
ya = int(input('Введите координату y для А '))
xb = int(input('Введите координату x для Б '))
yb = int(input('Введите координату y для Б '))
if (0 < xa < 9) and (0 < ya < 9) and (0 < xb < 9) and (0 < yb < 9):
    if abs(xa - xb) == 2 and abs(ya - yb) == 1 or abs(xa - xb) == 1 and abs(ya - yb) == 2:
        print('Yes')
    else:
        print('No')
else:
    print('Даннные введены не верно')