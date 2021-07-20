fhand = open('text_docs\\mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From':
        continue
    if len(words) >= 3 : print(words[2])
