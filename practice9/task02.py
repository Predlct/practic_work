
number = int(input('Введите число большее 2:\n'))

while number >= 2:
    number = number**(1/2)
    print(f'{number:.3f}')
