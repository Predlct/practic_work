
score_input = input('Введите рекорды Арины и Сергея:\n')

score = score_input.split()

if int(score[0])>int(score[1]):
    print(score[0])
else:
    print(score[1])
    