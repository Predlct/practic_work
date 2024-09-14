
number = input('Enter word:\n').strip()
tries = 0

print('\n'*75)

for i in range(0, 10):
    tries += 1
    number_try = input('Enter number:\n').strip().ljust(4,'*')
    quan_man = 0
    quan_women = 0

    for num in range(0, len(number)):
        if number[num] == number_try[num]:
            quan_man += 1
        elif number_try[num] in number:
            quan_women += 1

    if number == number_try:
        print('Win!')
        break
    print(f'Быков:{quan_man} Коров:{quan_women}')

if tries == 10:
    print('You are lose, hahaha!')
