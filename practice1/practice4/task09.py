
if input('Cобавка короткошерстной породы?\n').lower() == 'да':
    if input('Рост собаки менее 50 см?\n').lower() == 'да':
        if input('У собаки короткий хвост?\n?').lower() == 'да':
            print('английский бульдог')
        else:
            if input('У собаки длинные уши?\n').lower() == 'да':
                print('гончая')
            else:
                if input('У собаки короткое тело?\n').lower() == 'да':
                    print('мопс')
                else:
                    print('чихуахуа')
    else:
        if input('Собака весит более 50 к?\n').lower() == 'да':
            print('датский дог')
        else:
            print('фоксхаунд')
else:
    if input('Рост собаки менее 50 см?\n').lower() == 'да':
        if input('У собаки доброжелательный характер?\n').lower() == 'да':
            print('кокер-спаниэль')
        else:
            print('ирландский сеттер')
    else:
        if input('У собаки рост менее 70 см?\n').lower() == 'да':
            if input('У собаки длинные уши?\n').lower() == 'да':
                print('большой вандейский грифон')
            else:
                print('колли')
        else:
            if input('Окрас рыжий с белыми отметинами?\n').lower() == 'да':
                print('сенбернар')
            else:
                if input('Белоснежный окрас?\n').lower() == 'да':
                    print('ирландский волкодав')
                else:
                    print('ньюфаундленд')
                    