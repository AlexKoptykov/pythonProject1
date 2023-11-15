from math import sqrt
from random import  randint

# a = int(input('a? '))
# b = int(input('b? '))
# c = int(input('c? '))
a = randint(3, 5)
b = randint(3, 5)
c = randint(3, 5)
p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print(f'{s:.6}')