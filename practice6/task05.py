
chess_letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

move_input = input('Введите ход:\n')

move = move_input.split('-')


if move[1][0] and int(move[1][1]) in chess_letters:
    check_one = abs(int(chess_letters[move[0][0]]) - int(chess_letters[move[1][0]])) or abs(int(move[0][1]) - int(move[1][1]))
    check_two = abs(int(chess_letters[move[0][0]]) - int(chess_letters[move[1][0]])) + abs(int(move[0][1]) - int(move[1][1]))
    if check_one > 2:
        print('Ошибка')
    elif check_two == 3:
        print('Верно')
    else:
        print('Ошибка')
else:
    print('Невозможный ход')
