

with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as f2:
        average_january = sum(f.readlines()[0:31]) / 31
        average_february = sum(f.readlines()[31:60]) / 29
        average_march = sum(f.readlines()[60:91]) / 31
        average_april = sum(f.readlines()[91:121]) / 30
        average_may = sum(f.readlines()[121:152]) / 31
        average_june = sum(f.readlines()[152:182]) / 30
        average_july = sum(f.readlines()[182:213]) / 31
        average_august = sum(f.readlines()[213:244]) / 31
        average_september = sum(f.readlines()[244:274]) / 30
        average_october = sum(f.readlines()[274:305]) / 31
        average_november = sum(f.readlines()[305:335]) / 30
        average_december = sum(f.readlines()[335:366]) / 31
        f2.write(f'{average_january}\n{average_february}\n{average_march}\n{average_april}\n{average_may}\n'
                 f'{average_june}\n{average_july}\n{average_august}\n{average_september}\n{average_october}\n'
                 f'{average_november}\n{average_december}\n')
