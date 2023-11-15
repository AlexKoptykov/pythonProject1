a = int(input('Введиет первое число '))
b = int(input('Введите второе число '))
if a > b:
    min_num = a
    max_num = b
else:
    min_num = b
    max_num = a
print(str(max_num) + str(min_num), end="")