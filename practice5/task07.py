
quantity_input = input('Введите данные станций:\n')

quantity = quantity_input.split()

if int(quantity[1]) < int(quantity[2]):
    print(f'{int(quantity[1]) - int(quantity[2]) - 1} станций')
else:
    print(f'{int(quantity[0]) - int(quantity[1]) + int(quantity[2]) - 1} станций')