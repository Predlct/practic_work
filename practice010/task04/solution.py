
with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as f2:
        for line in f.readlines():
            if len(line[:-1]) > 20:
                f2.write(line)