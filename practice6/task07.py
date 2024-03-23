
quantity = int(input('Введите количество суш:\n'))

if quantity % 7 == 0:
    print('Да')
elif quantity % 12 == 0:
    print('Да')
else:
    while True:
        if quantity % 5 == 0:
            print('Да')
            break
        else:
            if quantity > 5:
                quantity -= 7
            else:
                print('Нет')
                break