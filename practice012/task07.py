
result = 'M' * (10**10)

for i in input('Enter text:\n').split():
    if len(i) == min(len(result), len(i)):
        result = i
print(result)

