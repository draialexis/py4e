fhand = open('text_docs\mbox-short.txt')
count = 0

for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    count = count + 1
    print(words[1])

print('Emails received:', count)
