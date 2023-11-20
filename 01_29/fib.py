n = int(input())
fib1 = fib2 = 1 # два соседних числа
print(fib1, fib2, sep='; ', end='; ')
c = 3
while c < n:
 fib2 = fib1 + fib2 # новое число
 fib1 = fib2 - fib1 # число предыдущее новому
 c += 1
 print(fib2, end='; ')
print(fib1 + fib2) # n-е число без ; в конце
