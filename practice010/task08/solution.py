
with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as f2:
        case = list(map(int, f.readlines()))
        average_january = sum(case[0:31]) / 31
        average_february = sum(case[31:60]) / 29
        average_march = sum(case[60:91]) / 31
        average_april = sum(case[91:121]) / 30
        average_may = sum(case[121:152]) / 31
        average_june = sum(case[152:182]) / 30
        average_july = sum(case[182:213]) / 31
        average_august = sum(case[213:244]) / 31
        average_september = sum(case[244:274]) / 30
        average_october = sum(case[274:305]) / 31
        average_november = sum(case[305:335]) / 30
        average_december = sum(case[335:366]) / 31
        f2.write(f'{average_january}\n{average_february}\n{average_march}\n{average_april}\n{average_may}\n'
                 f'{average_june}\n{average_july}\n{average_august}\n{average_september}\n{average_october}\n'
                 f'{average_november}\n{average_december}\n')
