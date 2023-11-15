a = int(input('Введите значение A '))
b = int(input('Введите значение B '))
c = int(input('Введите значение C '))
p = (a + b + c) / 2
s = (p  * (p - a) * (p - b) *(p - c)) ** 0.5
print(f'{s:.6}')