# print('Введите часы,минуты и секунды ')
# h1 = int(input())
# m1 = int(input())
# s1 = int(input())
# print(h1,m1,s1)

print('Введите часы:минуты:секунды ')
# t = input()
# h1, m1, s1 = t.split(':')
# print(h1, m1, s1)
# print(int(h1)+24)
# h1 = int(h1)
# m1 = int(m1)
# s1 = int(s1)
# print(type(h1))
h1, m1, s1 = map(int, input().split(':'))
print(h1+5)