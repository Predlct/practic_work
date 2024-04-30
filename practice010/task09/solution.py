import os
os.mkdir('simple')

with open('input.txt', 'r') as f:
    with open('simple\\output.txt', 'w') as f2:
        for i, line in enumerate(f.readlines()):
            if i//2 == 0:
                f2.write(line)

