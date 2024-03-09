
input_fish = input('Введите сколько поймал первый и второй рыбак?\n')

fish = input_fish.split()

if int(fish[0])>int(fish[1]):
    print(fish[1])
else:
    print(fish[0])