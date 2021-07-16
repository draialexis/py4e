fname = input('Enter a file name: ')
furl = 'text_docs\\' + fname + '.txt'

try:
    fhand = open(furl)
except:
    print('In the industry, we call that a woopsie')
    quit()

for line in fhand:
    print(line.strip().upper())
