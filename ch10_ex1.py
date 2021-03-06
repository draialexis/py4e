fname = input('Enter a file name: ')
furl = 'text_docs\\' + fname

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

max_count = max(list(emails.values()))
for email, count in emails.items():
    if count == max_count:
        print(email, count)
