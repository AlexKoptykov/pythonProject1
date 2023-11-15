s = int(input('Введите число '))
h = s // (60 ** 2)
m = s % (60 ** 2) // 60
s = s % 60
print(h,m,s, sep=':')
print(f'{h:02}:{m:02}:{s:02}')