
answer = int(input('Введите ответ:\n'))

while answer >= 2:
    answer = answer/2
else:
    if answer == 1:
        print('верно')
    else:
        print('неверно')