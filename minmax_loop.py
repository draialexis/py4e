greatest = None
smallest = None

while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    try:
        num = float(inp)
        if greatest is None or num > greatest:
            greatest = num
        if smallest is None or num < smallest:
            smallest = num
    except:
        print('Invalid input')

    print('greatest so far:', greatest, '; smallest so far:', smallest, 'last value added:', num)

print('max:', greatest, '; min:', smallest)
