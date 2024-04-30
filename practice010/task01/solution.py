

with open('input.txt', 'r') as f:
    result = f.read().upper()

with open('output.txt', 'w') as f:
    f.write(result)
