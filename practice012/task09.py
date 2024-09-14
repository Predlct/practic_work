
text = input('Enter text:\n').split()

for i in text:
    if text.count(i) == 2:
        print(i)
        break
