
cost = input('Введите цены на шоколад:\n' )

total_cost = sum(map(int, cost.split()))

print(total_cost)