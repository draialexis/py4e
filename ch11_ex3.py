import re
import urllib.request

url = 'http://py4e-data.dr-chuck.net/regex_sum_1283124.txt'
file = urllib.request.urlopen(url)

sum = 0

for line in file:
    line = line.decode('utf-8')
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        for thing in x:
            sum += int(thing)

print(sum)
