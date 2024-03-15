
pincod = input('Введите пинкод:\n')

if pincod[0] == pincod[1] or pincod[0] == pincod[2] or pincod[0] == pincod[3] or pincod[1] == pincod[2] or pincod[1] == pincod[3] or pincod[2] == pincod[3]:
    print('ERROR')
else:
    if int(pincod) > 9999:
        print('ERROR')
    else:
        if int(pincod) < 1000:
            print('ERROR')
        else:
            if int(pincod) > 1900:
                if int(pincod) < 2050:
                    print('ERROR')
                else:
                    print('OK')
            else:
                print('ОК')