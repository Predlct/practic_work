
with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as f2:
        for line in f.readlines():
            if line[0].upper() == 'A':
                f2.write(line)
