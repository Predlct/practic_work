
time = int(input('Введите число от 1 до 86400:\n'))



print(f'Текущее время: {time//3600}.{(time/60)%60:.0f}.{time%60:.0f}')