
ice_cream = int(input('Введите количество мороженного:\n'))
people = 2

while ice_cream % people != 0:
    people += 1
print(people)

