x = int(input())
y = int(input())
n = 0
if x > 10000 and y > 10000:
    print('Не правельно введены данные')
elif x <= y:
    if y // x == 1:
        print('Yes')
    elif y == 10000 and x == 1:
        print('Yes')
    else:
        print('No')
