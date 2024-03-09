
score_input = input('Введите счет игры двух комманд через ":" :\n ')

score = score_input.split(':')

if int(score[0])<int(score[1]):
    print(2)
else:
    if int(score[0])>int(score[1]):
        print(1)
    else:
        print(0)
