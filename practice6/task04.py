
chess_letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

chess_square = input('Введите наименование шахматной клетки:\n')

if chess_letters[chess_square[0]] % 2 == 1:
    if int(chess_square[1]) % 2 == 1:
        print('Белый')
    else:
        print('Черный')
else:
    if int(chess_square[1]) % 2 == 0:
        print('Белый')
    else:
        print('Черный')
