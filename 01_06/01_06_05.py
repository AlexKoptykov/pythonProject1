#Иногда такие шаблоны встречаются и в других сферах,
# например в аттестации обучающихся в школе. Напишите программу,
# которая принимает в первой строке ФИО ученика,
# а дальше в трёх других строках оценки по информатике,
# математике и физике, после чего выводит результат в следующей форме:
#Ученик [ФИО] получил за год:
# по информатике - [оценка по информатике]
# по математике - [оценка по математике]
# по физике - [оценка по физике]

name = input('ФИО')
a = int(input('Оценка по информатике'))
b = int(input('Оценка по математике'))
c = int(input('Оценка по физре'))
print(f'{name}')
print(f'{a}')
print(f'{b}')
print(f'{c}')