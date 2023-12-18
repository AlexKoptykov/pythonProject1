v = input('Составленое слово Вити ')
p = input('Составленое слово Пети ')
z = set()
if len(v) == len(p):
    print('ALL')
else:
    for s in v:
        if s not in z:
            cv = v.count(s)
            cp = p.count(s)
            print(s*(cv-cp), end=' ')
            z.add(s)