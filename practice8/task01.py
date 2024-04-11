
number = int(input('Введите число:\n'))
result = 0
while number != -1:
    previous_number = number
    number = int(input('Введите число:\n'))
    if result < previous_number:
        if number > previous_number:
            result = number
        else:
            result = previous_number
        
print(result)