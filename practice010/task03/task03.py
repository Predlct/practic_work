
with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as f2:
        for line in f.readlines():
            f2.write(line[0])