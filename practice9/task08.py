
number = int(input('Enter natural number:\n'))

quantity = 0

for i in range(1, round(number**(1/2))+1+1):
    for n in range(1, round(number**(1/2))+1+1):
        if i**2 + n**2 == number:
            quantity += 1

print(f'{quantity/2:.0f}')