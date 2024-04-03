
temperature = float(input('\n'))

previous_temperature = temperature
i = 0
while temperature > 0:
    if temperature < previous_temperature:
        i += 1
        previous_temperature = temperature
        temperature = float(input('\n'))
    else:
        previous_temperature = temperature
        temperature = float(input('\n'))
print(i)