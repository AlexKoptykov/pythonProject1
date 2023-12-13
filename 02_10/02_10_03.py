n = int(input('Кол-во элементов в коллекции? '))
collect = set()
for i in range(1, n+1):
    collect2 = (input(f'{i} - ый элемент? '))
    if collect2 in collect:
        print('Есть')
    else:
        print('Нет')
        collect.add(collect2)