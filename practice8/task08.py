

number = '123456789'
number_two = '1111111111'



for i in range(1, 9+1):
    print(f'{number[:i]} * 8 + {i} = {int(number[:i]) * 8 + i}', end='\n')

for i in range(1, 9+1):
    print(f'{number[:i]} * 9 + {i + 1} = {number_two[:i + 1]}', end='\n')

for i in range(1, 9+1):
    print(f'{number_two[:i]} * {number_two[:i]} = {int(number_two[:i])*int(number_two[:i])}', end='\n')
