
number = int(input('Enter max quantity of dot:\n'))
quantity = 0

for i in range(1, number+1):
    quantity += (number*i)
print(quantity)