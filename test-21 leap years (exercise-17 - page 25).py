year = int(input('Enter a year: '))

num = 0
for i in range(1600, year+1, 1):
    if(i%4 == 0):
        if(i%100 == 0):
            if(i%400 == 0):
                num += 1
        else:
            num += 1

print(num)
