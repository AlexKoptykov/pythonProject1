n = int(input('Кол-во продуктов? '))
p = [0] * n
for i in range(n):
    p[i] = input('? ')
for i in range(n-1, -1, -1):
    print(p[i])