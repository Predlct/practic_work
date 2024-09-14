
words = input('Enter words:\n').split()

for i in range(1, len(words)):
    if words[i] == words[-1]:
        print(('Петя ' if i % 2 == 0 else 'Вася ') + 'победил')
    elif words[i][0] != words[i-1][-1]:
        print(('Вася ' if i % 2 == 0 else 'Петя ') + 'победил')


