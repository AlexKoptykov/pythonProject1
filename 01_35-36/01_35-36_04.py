n = int(input())
a = input()
b = a.split()
b_n = list(map(int, b))
b_n.sort()
t = b_n[-1]
i = len(b_n) - 1
while i >= 0:
    if b_n[i] < t:
        print(b_n[i])
        break
    i = i - 1