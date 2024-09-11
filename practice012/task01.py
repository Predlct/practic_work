
text = input('Введите текст:\n')
m = 0

for i in range(1, len(text)):
    if text.count(' ' * i) != 0:
       m = i
    else: break

print(m)