c = int(input(' '))
s = c//100
d = (c-(s*100))//10
print(f'true' if s>d else 'false')