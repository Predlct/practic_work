
volume = int(input('Введите ограничение по объему:\n'))

len = 1

while len**3 <= volume:
    print(f'{len**3}', end=' ')
    len +=1
