count = 0
while True:
    nota = input('Введите ноту ')
    if nota == 'END':
        break
    elif nota[0] == 'C':
        count += 1
print(count)
