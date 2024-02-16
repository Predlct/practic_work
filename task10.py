
number = input('Номер вашего рейса?\n')

company_rus = input('Название авиакопмпании?(На русском языке)\n')

company_eng = input('Название авиакопмпании?(На английском языке)\n')

arrival_city_rus = input('Город прибытия?(На русском языке)\n')

arrival_city_eng = input('Город прибытия?(На английском языке)\n')

print('Заканчивается посадка на рейс', number, company_rus, 'до',arrival_city_rus)
print('This is the final boarding call for',company_eng, 'flight',number, 'to', arrival_city_eng)
