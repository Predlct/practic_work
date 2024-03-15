
weight = int(input('Введите вес:\n'))

height = int(input('Введите рост:\n'))

if weight/(float(height/100))**2 < 16:
    print(f'выраженный дефицит массы тела')
else:
    if weight/(float(height/100))**2 < 18.5:
        print(f'недостаточная масса тела')
    else:
        if weight / (float(height / 100)) ** 2 < 25:
            print(f'норма')
        else:
            if weight / (float(height / 100)) ** 2 < 30:
                print(f'избыточная масса тела')
            else:
                if weight / (float(height / 100)) ** 2 < 35:
                    print(f'ожирение первой степени')
                else:
                    if weight / (float(height / 100)) ** 2 < 40:
                        print(f'ожирение второй степени')
                    else:
                        print(f'ожирение третьей степени')
