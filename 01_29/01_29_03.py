c = float(input('Введите частоту ноты '))
s = ''
while c >= 220:
        s += str(c) + '\n'
        c = float(input('Введите частоту ноты '))
print(s)