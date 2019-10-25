kilograms = int(input('Enter weight: '))

pound = int(kilograms * 2.20462)
if(pound % 10 <= 5):
    pound -= pound % 10
else:
    pound += 10 - (pound % 10)
    
print(pound)
