
income = int(input('Введите доход:\n'))
quantity = 0
summ = 0
while income != 0:
    summ += income
    quantity += 1
    income = int(input('Введите доход:\n'))

print(summ/quantity)
