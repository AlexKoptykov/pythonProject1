n = int(input('Кол-во элементов в коллекции? '))
collect = set()
for i in range(1, n+1):
    collect.add(input(f'{i} - ый элемент? '))
print(*collect) # collect - распаковка
new_element = input(f'Новый элемент? ')
if new_element in collect:
    print('Такой элемент уже есть. Не нужен!')
else:
    print('Наконец-то, это то, чего не хватало!')
    collect.add(input(f'{i} - ый элемент? '))
    print(*collect)