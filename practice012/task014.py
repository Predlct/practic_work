
clue = input('Enter clue for you word:\n')
word = input('Enter word:\n').strip()
tries = 0
bag =[]

print('\n'*75, clue,'\n'+'*'*len(word))

for i in range(0, 10):
    tries += 1

    word_or_letter_try = input('\n A one letter or word:\n').strip().lower()
    if word_or_letter_try in word.lower():
        bag.append(word_or_letter_try)

    if len(word_or_letter_try) != 0 and word_or_letter_try == word.lower():
        if tries <= 3:
            print('Perfect, You are win!')
        print('Win!')
        break

    for letter in word:
        if letter.lower() not in bag:
            print('*', end='')
        else:
            print(letter, end='')

if tries == 10:
    print('Awfully, you are lose! ')

