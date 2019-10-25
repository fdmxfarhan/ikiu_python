second = int(input('Second:'))

minute = second // 60
second -= minute * 60

print 'It is', minute, 'minutes and', second, 'seconds.'
