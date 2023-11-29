a = int(input('Введите четырех значное число '))
b = int(input('Введите четырех значное число '))
for i in range(a, b + 1):
    t = i // 1000
    s = (i // 100) % 10
    d = (i // 10) % 10
    e = i % 10
    if t == e and s == d:
        print(i)