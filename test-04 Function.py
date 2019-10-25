# function
from math import *
def f(a,b):
    result = 0.0
    for i in range(1,b,1):
        result += (a**i) / factorial(i)
    return(result)

print 'f(1,5)=', f(1 , 5)
print 'f(1,10)=', f(1 , 10)
print 'f(2,100)=', f(2 , 100)
