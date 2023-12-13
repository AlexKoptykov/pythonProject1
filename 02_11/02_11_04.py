n = int(input('Количество видов компонентов '))
s1 = set()
for i in range(n):
    s1.add(input())
k1 = int(input('Количество видов компонентов для 1-й схемы '))
s2 = set()
for t in range(k1):
    s2.add(input())
k2 = int(f'Количество видов компонентов для 2-й схемы {n-k1}')
s3 = set()
for t in range(k2):
    s3.add(input())
if s2 in s3:
    print('НЕЛЗЯ СОБРАТЬ')
else:
    print('МОЖНО СОБРАТЬ')