import re
fname = input('Enter file:')
if not fname is None:
    try:
        fhand = open('text_docs\\' + fname)
    except:
        print('woops')
        quit()

sum, counter = 0, 0

for line in fhand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        for thing in x:
            sum += int(thing)
            counter += 1

print(int(sum/counter))
