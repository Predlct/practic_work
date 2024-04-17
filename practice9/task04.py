
quantity = int(input('Введите количество веревок для этой команды:\n'))
number = 0


while quantity != 0:
    if quantity % 4 == 0:
        number += 1
        quantity = int(input('Введите количество веревок для этой команды:\n'))
    else:
        quantity = int(input('Введите количество веревок для этой команды:\n'))
print(number)


