from random import  randint

a = randint(1, 6)
b = randint(1, 6)
a += randint(1, 6)
b += randint(1, 6)
print("Первый кубик" * int(a > b) + "Второй кубик" * int(a < b) + "Одинаково очков" *  int(a == b))