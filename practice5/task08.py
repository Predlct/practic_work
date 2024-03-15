
knats = int(input('Введите количество кнатов:\n'))

add_knats = knats%29
sikls = knats%(29*17)//29

galleon = knats//(29*17)


if galleon == 0:
    print(f'{sikls} сиклей\n'
          f'{add_knats} кнатов')
else:
    if sikls == 0:
        print(f'{galleon} галлеонов\n'
          f'{add_knats} кнатов')
    else:
        if add_knats == 0:
            print(f'{galleon} галлеонов\n'
          f'{sikls} сиклей')
        else:
            print(f'{galleon} галлеонов\n'
                  f'{sikls} сиклей\n'
                  f'{add_knats} кнатов')



