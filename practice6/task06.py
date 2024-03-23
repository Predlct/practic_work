
quantity_input = input('Введите количество малышей, '
                       'вместимость карусели и длину сеанса через пробел:\n')

quantity = quantity_input.split()

if int(quantity[0]) < int(quantity[1]):
    print(f'{2*int(quantity[2])}')
else:
    if int(quantity[0]) % int(quantity[1]) == 0:
        print(f'{(int(quantity[0]) / int(quantity[1]))*2*int(quantity[2]):.0f}')
    else:
        print(f'{(int(quantity[0]) // int(quantity[1]) + 1) * 2 * int(quantity[2]):.0f}')
