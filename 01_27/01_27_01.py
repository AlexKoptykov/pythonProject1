mi, ma = 1000, -1000
while True:
    n = int(input())
    if n == 0:
        break
    if n < mi:
        mi = n
    if n > ma:
        ma = n
print('min =', mi, '\nmax =', ma)
