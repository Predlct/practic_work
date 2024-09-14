
text = input('Enter text:\n').split()

for word in text[1:]:
    quan = 0
    for i in word:
        if word.count(i) == 1:
            quan += 1
        if quan == len(word) and word != text[0]:
            print(word, end=' ')
