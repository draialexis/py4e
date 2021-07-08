total = 0.0
count = 0.0
average = 0.0

while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    try:
        num = float(inp)
        count = count + 1
        total = total + num
    except:
        print('Invalid input')

if not count == 0:
    average = total / count

print('total:', total, '; count:', count, '; average:', average)
