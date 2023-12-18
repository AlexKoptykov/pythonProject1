s = '0123456789ABCDEF'
n = set(input('Введите 16 - ричное число? '))
for i in range (len(s)):
    if s[i] not in n:
        print(s[i], end=' ')