import datetime

with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as f2:
        case = f.readlines()
        date_now = datetime.datetime(2024, int(case[0].split('.')[1]), int(case[0].split('.')[0]))
        for line in case[2:]:
            date_bag = datetime.datetime(2024, int(line.split(' ')[1][:-1].split('.')[1]),
                                         int(line.split(' ')[1][:-1].split('.')[0]))
            delta = date_now - date_bag
            if delta.total_seconds() // (60*60*24) > 3:
                f2.write(line)
