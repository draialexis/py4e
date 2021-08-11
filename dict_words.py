import string

fname = input('Enter a file name: ')
furl = 'text_docs\\' + fname + '.txt'

try:
    fhand = open(furl)
except:
    print('In the industry, we call that a woopsie')
    quit()

words = dict()

for line in fhand:
    line = line.rstrip()
    line = line.lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    for word in line.split():
        words[word] = words.get(word, 0) + 1
print(words)

vals = list(words.values())
max_val = max(vals)

for word, count in words.items():
    if count == max_val:
        print('Most frequent word:', word, '~~', count)
