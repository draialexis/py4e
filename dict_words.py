fhand = open('text_docs\words.txt')
words = dict()

for line in fhand:
    for word in line.split():
        words[word] = '_'

print(words)
