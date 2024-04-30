
with (open('input.txt', 'r') as f):
    with open('output.txt', 'w') as f2:
        n = f.readlines()
        try:
            result = str(int(n[0]) / int(n[1]) + int(n[2]))
            f2.write(result)
        except ValueError:
            f2.write('data error')
        except ZeroDivisionError:
            f2.write('division by 0')
