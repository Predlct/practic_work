
data_input = input('Введите последовательность трех чисел:\n') # 1 число - количество чисел 2 в строке

data = data_input.split()

print(f'Результат - {int(data[0]*int(data[1]))*int(data[2])}')
