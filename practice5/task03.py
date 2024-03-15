
number = input('Введите число:\n')

if int(f'{number[3]}{number[2]}{number[1]}{number[0]}') == int(number):
    print('Настоящее')
else:
    print('Кривое')

