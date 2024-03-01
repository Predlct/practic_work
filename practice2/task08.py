
input_quantity = input('Введите количество друзей и конфет: \n')

quantity = input_quantity.split()

print(f'{ int(quantity[1])//(int(quantity[0])+1)}')
