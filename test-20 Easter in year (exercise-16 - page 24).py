from math import floor

y = int(input('Enter a year: '))

C = y // 100
m = (15 + C - floor(C/4) - floor((8*C + 13) / 25))% 30
n = (4  + C - floor(C/4))% 7

a = y%4
b = y%7
c = y%19
d = (19*c + m)% 30
e = (2*a + 4*b + 6*d + n)% 7

print(e)
