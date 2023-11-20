c = input('Введите цвет ')[0].upper()
s = ''
while c == 'С' or c == 'Ж' or \
        c == 'З' or c == 'О' or c == 'К' or c == 'Ф':
        s += c + '\n'
        c = input('Введите цвет ')[0].upper()
print(s)

