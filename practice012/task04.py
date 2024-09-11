
text = input('Enter text:\n')

for i in text:
    if text.count(i) == 3:
        print(i)
        break
