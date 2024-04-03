
string = input('Ввдите строку:\n')
i = 2
while i <= len(string):
    word = string[i]
    print(f'{word}', end='')
    i += 3
