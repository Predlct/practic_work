
xc_1 = int(input('Введите координату x центра первой окружности:\n'))

yc_1 = int(input('Введите координату y центра первой окружности:\n'))

r_1 = int(input('Введите радиус первой окружности:\n'))

xc_2 = int(input('Введите координату x центра второй окружности:\n'))

yc_2 = int(input('Введите координату y центра второй окружности:\n'))

r_2 = int(input('Введите радиус второй окружности:\n'))

if ((xc_1 - xc_2)**2 + (yc_1 - yc_2)**2)**(1/2) > (r_1 + r_2):
    print('Окружности лежат одна вне другой, не касаясь')
elif ((xc_1 - xc_2)**2 + (yc_1 - yc_2)**2)**(1/2) == (r_1 + r_2):
    print('Окружности имеют внешнее касание')
else:
    if ((xc_1 - xc_2)**2 + (yc_1 - yc_2)**2)**(1/2) + min(r_1,r_2) > max(r_1,r_2):
        print('Окружности пересекаются')
    elif ((xc_1 - xc_2)**2 + (yc_1 - yc_2)**2)**(1/2) + min(r_1,r_2) == max(r_1,r_2):
        print('Окружности имеют внутрнее касание')
    else:
        print('Одна окружность лежит внутри другой, не касаясь')
