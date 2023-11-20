C = input('Введите цвет green, red, blue ')[0].upper()
A = int(input('Введите начальную интенсивнось '))
B = int(input('Введите конечную интенсивность '))
for n in range(A, 1 + B):
    print(f'{C}{n}')
