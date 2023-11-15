a = int(input('Введите 3-х значное число '))
br = a // 100
# print(f'За завтраком выпил {br}')
# lanch = (a - br * 100) // 10
lanch = (a % 100) // 10
# print(f'За обедом выпил {lanch}')
din = a % 10
# print(f'За ужином выпил {din}')
print(br + lanch + din)
