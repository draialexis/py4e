fhand = open('text_docs\\romeo.txt')

unique_words = []

for line in fhand:
    words = line.split()
    for word in words:
        if not word in unique_words:
            unique_words.append(word.lower())

unique_words.sort()
print(unique_words)
