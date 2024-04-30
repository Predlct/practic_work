
with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as f2:
        n = (f.readline()[0])
        try:
                if len(f.readlines()) - 1 == int(n):
                        f2.write('YES')
                else:
                        f2.write('NO')
        except ValueError:
                f2.write('ERROR')
