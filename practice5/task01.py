year = int(input('Введите год:\n'))
if year%4 == 1 or 2 or 3 :
    print('365')
else:
    if year%400 == 0:
        print('366')
    else:
        print('365')
