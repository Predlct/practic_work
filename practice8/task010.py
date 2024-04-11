
summ = 0

for number in range(2, int(input('Введите число:\n'))+1):
    for i in range(1, number + 1):
        if number % i == 0:
            summ += i
    if summ == 2 * number:
        print(number)
    summ = 0