
number = int(input('Введите число:\n'))
quantity = 0

for i in range(2, number + 1):
    for i2 in range(2, i):
        if i % i2 == 0:
            quantity += 1
    if quantity == 0:
        print(i)
    quantity = 0
