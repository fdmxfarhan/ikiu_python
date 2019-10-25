width = int(input('Enter width: '))
height = int(input('Enter height: '))

for i in range(width * height):
    print(i%10, end=' ')
    if((i+1)%width == 0 and i != 0):
        print()
