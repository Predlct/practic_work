
number = int(input('Введите количество кубиков, не превыщающее 100:\n'))

for i in range(1, number+1):
    if number == i:
        if i == 1 or i == 2:
            print(1)
        elif i == 3:
            print(2)
        else:
            print(number-2)



