
quantity_input = input('Введите количество подданых за каждый день через пробел:\n')

quantity = quantity_input.split()

if quantity[0] == quantity[1] and quantity[0] == quantity[2]:
    print('3')
else:
    if quantity[0] == quantity[1] or quantity[0] == quantity[2] or quantity[1] == quantity[2]:
        print('2')
    else:
        print('Повторений нет')



