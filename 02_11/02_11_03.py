n = int(input('Количество видов компонентов для 1-й схемы '))
m = int(input('Количество видов компонентов для 2-й схемы '))
k = int(input('Количество видов компонентов для 3-й схемы '))
s1 = set()
s2 = set()
s3 = set()
for i in range(n):
    s1.add(input())
for t in range(m):
    s2.add(input())
for t in range(k):
    s3.add(input())
s4 = s1 & s2 & s3
print(len(s4))