fname = input('Enter a file name: ')
furl = 'text_docs\\' + fname + '.txt'

try:
    fhand = open(furl)
except:
    if fname.lower() == 'na na boo boo':
        print('na na boo boo to you')
    else:
        print('woopsie')
    quit()

spam_conf_total = 0
count = 0
spam_conf_avg = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        start = line.find(' ')
        snum = line[start+1:]

        try:
            num = float(snum)
        except:
            print('something went wrong with', snum)

        count = count + 1
        spam_conf_total = spam_conf_total + num

if count > 0 :
    spam_conf_avg = spam_conf_total / count

print(round(spam_conf_avg, 12))
