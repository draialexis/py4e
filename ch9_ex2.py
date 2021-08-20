fname = input('Enter a file name: ')
furl = 'text_docs\\' + fname + '.txt'

try:
    fhand = open(furl)
except:
    print('nah-aah')
    exit()

days = dict()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        if len(words) >= 3:
            day = words[2]
            days[day] = days.get(day, 0) + 1

print(days)
