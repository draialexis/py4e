fname = input('Enter a file name: ')
furl = 'text_docs\\' + fname

try:
    fhand = open(furl)
except:
    print('nah-aah')
    exit()

times = dict()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        if len(words) >= 6:
            ftime = words[5]
            end = ftime.find(':')
            time = ftime[:end]
            times[time] = times.get(time, 0) + 1



l = list(times.items())
l.sort()

for time, count in l:
    print(time, count)
