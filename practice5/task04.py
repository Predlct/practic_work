
number = input('Введите число от 0 до 100:\n')

if int(number[-1]) == 0:
    print(f'{number} попугаев')
else:
    if int(number[-1]) == 1 :
        print(f'{number} попугай')
    else:
        if int(number[-1]) < 5:
            print(f'{number} попугая')
        else:
            print(f'{number} попугаев')