n = int(input('Кол-во элементов в коллекции? '))
collect = set()
y = 0
h = 0
for i in range(1, n+1):
    collect.add(input(f'{i} - ый элемент? '))
k = int(input('Кол-во элементов в коллекции? '))
collect = set()
for t in range (k):
    collect2 = (input('Кол-во элементов во 2-й коллекции? '))
    if collect2 in collect:
        y = y + 1
    else:
        h = h + 1
    print(f'{y} {h}')