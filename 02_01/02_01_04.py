s = input()
n = int(input())
print(s * n)
for i in range(0,n-2):
    print(s + ' ' * (n-2) + s)
print(s * n)