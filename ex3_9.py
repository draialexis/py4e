fname = input('Enter a file name: ')
furl = 'text_docs\\' + fname + '.txt'

try:
    fhand = open(furl)
except:
    print('nah-aah')
    exit()

emails = dict()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        if len(words) >= 2:
            email = words[1]
            emails[email] = emails.get(email, 0) + 1

print(emails)
