
data_input = input('Введите стоимость чашки кофе(в рублях и копейках) и количество купленных за день:\n')

data = data_input.split()

print(f'{int(data[0])*int(data[2]) + int(data[1])*int(data[2])//100} руб. {int(data[1])*int(data[2])%100} коп.')