def digits(inp):
    dot_pos = inp.find('.')
    count = 0
    if not dot_pos == -1:
        length = len(inp)
        count = length - (dot_pos + 1)

    return count

def switch_comas(inp):
    coma_pos = inp.find(',')
    if not coma_pos == -1:
        inp = inp.replace(',', '.')

    return inp

choice = input("Type 'c' to convert from 'Celsius' or 'f' to convert from 'Farenheit': ")
if choice.upper() == 'C':
    inp = input('Enter a temperature in Celsius: ')
    inp = switch_comas(inp)
    try:
        c_temp = float(inp)
        f_temp = c_temp * 9 / 5 + 32
        if digits(inp) == 0:
            print(int(f_temp))
        else:
            print(round(f_temp, digits(inp)))

    except:
        print('Invalid input -- please enter a number')

elif choice.upper() == 'F':
    inp = input('Enter a temperature in Farenheit: ')
    inp = switch_comas(inp)
    try:
        f_temp = float(inp)
        c_temp = (f_temp - 32) * 5 / 9
        if digits(inp) == 0:
            print(int(c_temp))
        else:
            print(round(c_temp, digits(inp)))

    except:
        print('Invalid input -- please enter a number')
        
else: print('Invalid input -- please choose the conversion type you want')
