# урок 10
# урок 5
word = input('Введите 2 слова ч/з пробел ')
pos = word.find(' ')
w1 = word[0:pos] #срез с 0 сим до pos
w2 = word[pos+1:] #срез с позиции pos+1
print(f'Слово {w1} имеет длинну {len(w1)}')
print(f'Слово {w2} имеет длинну {len(w2)}')