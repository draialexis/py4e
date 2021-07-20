numbers = []

while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    try:
        num = float(inp)
        numbers.append(num)
    except:
        print('Invalid input')

print('max:', max(numbers), '; min:', min(numbers))
