def fact(n):
    if(n == 1):
        return 1
    if(n == 2):
        return 2
    return(fact(n-1) * n)

a = int(input('Enter a number: '))
print(fact(a))
