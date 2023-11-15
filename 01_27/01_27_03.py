s = input('?')
text = ''
while s != '':
    text += s
    s = input('?')
if 'любовь' in text and 'кровь' in text:
    print('НЕ ХОРОШЕЕ')
else:
    print('ХОРОШЕЕ')