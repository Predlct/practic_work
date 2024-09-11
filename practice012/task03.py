
text = input('Enter text:\n')
quan = 0

for i in text:
    if text.count(i) == 1:
        quan += 1

print(quan)
