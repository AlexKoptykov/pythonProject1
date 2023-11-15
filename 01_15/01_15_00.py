x = int(input('Введите четырёхзначное число: '))
a = x // 1000
b = x // 100 % 10
c = x // 10 % 10
d = x % 10
print(a, b, c, d, sep='-')
print(a ** 2, b ** 2, c ** 2, d ** 2, sep='\n')