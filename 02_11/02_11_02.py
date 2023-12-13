n = int(input('Количество видов компонентов для 1-й схемы '))
m = int(input('Количество видов компонентов для 2-й схемы '))
s1 = set()
s2 = set()
for i in range(n):
    s1.add(input())
for t in range(m):
    s2.add(input())
s3 = s1 & s2
print(len(s3))