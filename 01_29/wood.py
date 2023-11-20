x = float(input())
r = 4
for y in range(1, 8):
    v = int(input('Введи число из отрезка [3, 26] '))
    if 3 <= v < 12:
        x -= 0.05 * x
        r += x
    elif 12 <= v < 16:
        x += 0.05 * x
        r += x
    elif 16 <= v <= 26:
        x += 0.03 * x
        r += x
 print(f'Прошёл, {y}, год. Высота -, {r}, см., Выросло на, {x}, см.')
