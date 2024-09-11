
text = input('Введите текст:\n')
quan = 0

for i in text:
    quan = max(text.count(i), quan)

print(quan)