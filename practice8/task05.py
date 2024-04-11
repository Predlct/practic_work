
summ = 0

quantity = 0

for number in range(2, int(input('Введите число:\n'))-1):
    for i in range(1, number + 1):
        if number % i == 0:
            summ += i
    if summ == 2 * number:
        quantity += 1
    summ = 0

print(quantity)
