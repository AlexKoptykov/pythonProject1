n = int(input('Введите номер фильма '))
print('Введите 0 или 1 в зависимости от наличие объектов в кадре')
object_in_kadr = int(input('0 или 1 '))
count_ob_in_scene = 0
while object_in_kadr != -1:
    count_ob_in_scene += object_in_kadr
    object_in_kadr = int(input('0 или 1 '))

print('YES' if object_in_kadr % n == 0 else 'NO')