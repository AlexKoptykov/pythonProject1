n = int(input('Кол-во элементов в коллекции? '))
collect = set()
for i in range(1, n+1):
    collect.add(input(f'{i} - ый элемент? '))
print(len(collect))