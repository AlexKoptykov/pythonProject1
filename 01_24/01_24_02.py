n = int(input('Количество мест чет '))
k = int(input('Место Васи '))
if k<=n/2:
    z = n / 2 - k
else:
    z = n / 2 - (n - k + 1)
    print(f'запнувшихся {z}')
