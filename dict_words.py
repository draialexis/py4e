fname = input('Enter a file name: ')
furl = 'text_docs\\' + fname + '.txt'

try:
    fhand = open(furl)
except:
    print('In the industry, we call that a woopsie')
    quit()

words = dict()

for line in fhand:
    for word in line.split():
        words[word] = words.get(word, 0) + 1
print(words)
