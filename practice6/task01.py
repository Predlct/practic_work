
r = 6.5

carpet_input = input('Введите размер ковра:\n')

carpet = carpet_input.split('x')

if ((int(carpet[0])/2)**2 + (int(carpet[1]))**2)**(1/2) > r:
    print('Нет')
else:
    print('Да')
