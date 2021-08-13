import string

fname = input('Enter a file name: ')
furl = 'text_docs\\' + fname

try:
    fhand = open(furl)
except:
    print('nah-aah')
    exit()

letters = dict()

for line in fhand:
    if len(line) == 0:
        continue
    line = line.rstrip()
    line = line.lower()
    for letter in line:
        if(letter.isalpha()):
            letters[letter] = letters.get(letter, 0) + 1

# Am I doing DSU, daddy? o_o
lkv = list(letters.items())
lvk = list()
for letter, count in lkv:
    lvk.append((count, letter))

lvk.sort(reverse=True)

for count, letter in lvk:
    print(letter, count)
