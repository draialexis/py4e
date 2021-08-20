fname = input('Enter a file name: ')
furl = 'text_docs\\' + fname + '.txt'

try:
    fhand = open(furl)
except:
    print('nah-aah')
    exit()

domains = dict()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        if len(words) >= 2:
            email = words[1]
            start = email.find('@')
            domain = email[start:]
            domains[domain] = domains.get(domain, 0) + 1

print(domains)

max_count = max(list(domains.values()))
for domain, count in domains.items():
    if count == max_count:
        print('Most frequent correspondent:', domain, '(count', count, ')')
