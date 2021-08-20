import re
fhand = open('text_docs\mbox.txt')
inp = input('Enter a regular expression: ')
counter = 0

for line in fhand:
    line = line.rstrip()
    if re.search(inp, line):
        counter += 1

print('mbox.txt had', counter, 'lines that matched', inp)
