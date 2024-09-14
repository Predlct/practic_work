
import keyword

string = input('Enter string:\n').strip()

if string[0].isalpha():
    if string not in keyword.kwlist:
        print('Good choice of name your variable')
    else:
        print('So bad, try again ')
else:
    print('So bad, try again ')
