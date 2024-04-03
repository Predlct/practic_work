
data_input = input('Введите данные через пробел N,K и R:\n')

data = data_input.split()

len = int(data[0])

quantity = 1

while len < int(data[2]):
    len = len*(int(data[1])/100 + 1)
    quantity += 1
print(quantity)
