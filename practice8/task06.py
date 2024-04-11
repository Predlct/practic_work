
number = int(input('Введите число:\n'))

for i in range(1, number + 1):
    print(' '*(number-i)+'*'*i, end='\n')