from random import randint
t = input('word? ')
n = int(input())
if n >= len(t):
    print('Index out of range')
else:
    print(t[n])
print(t[randint(0, len(t)-1)])