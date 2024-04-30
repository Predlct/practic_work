
with open('input.txt', 'r') as f:
    case = f.readlines()
    with open('input.txt', 'w') as f2:
        for line in case:
            if line != '100\n':
                f2.write(line)

