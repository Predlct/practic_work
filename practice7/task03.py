
number = int(input('Введите число:\n'))

while True:
    if int(str(number**(1/2)).split('.')[1]) == 0:
        print('Число является полным квадратом')
        break
    else:
        print('Число не является полным квадратом')
        number = int(input('Введите другое число:\n'))

