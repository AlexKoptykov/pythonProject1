n = int(input('Кол-во учеников? '))
all_lang = set()
one_lang = set()
for i in range(1, n+1):
    k = int(input(f'Кол-во языков {i}-го ученика: '))
    temp_lang = set()
    for j in range(1, k+1):
        l = input(f'{j} язык: ')
        all_lang.add(l)
        temp_lang.add(l)
    if i == 1:
        one_lang.update(all_lang)
    else:
        one_lang = one_lang & temp_lang
print('Языки которые знает хотябы один ученик')
print(*all_lang)
print('Языки которые, изучают все ученики')
print(*one_lang)