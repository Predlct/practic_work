
string1 = 'None'
string2 = 'Prices'
string3 = 'Countable'

for i in string1:
    if i not in string2 + string3:
        print(i, end=' ')

for i in string2:
    if i not in string1 + string3:
        print(i, end=' ')

for i in string3:
    if i not in string1 + string2:
        print(i, end=' ')
