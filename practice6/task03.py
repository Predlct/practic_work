
square_input = input('Введите размер оцепления:\n')

quantity = int(input('Введите количество кварталов:\n'))

square = square_input.split('x')

area = int(square[0])*int(square[1]) - int(min(square[0],square[1]))
while area > quantity:
    if area%quantity == 0:
        print('Успешно')
        break
    else:
        area -= int(min(square[0],square[1]))
