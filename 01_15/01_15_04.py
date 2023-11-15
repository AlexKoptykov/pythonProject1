x = int(input('Введите 3-х значное число '))
s = x // 100
d = x % 100 // 10
e = x % 10
sum = s + d + e
print(f'{s}+{d}+{e}={sum}')
print(s,d,e, sep='+', end='=')
print(sum)