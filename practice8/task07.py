
number = input('Введите целое число:\n')

while not number.isdigit():
    number = input('Ошибка, Введите число:\n')

print(f'Введено целое число: {number}')
