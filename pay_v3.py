def warn_and_exit():
    print('Error, please enter numeric input')
    quit()

def switch_comas(inp):
    coma_pos = inp.find(',')
    if not coma_pos == -1:
        inp = inp.replace(',', '.')

    return inp

inp = input('Enter Hours: ')
s_hours = switch_comas(inp)
try: total_hours = float(s_hours)
except: warn_and_exit()

inp = input('Enter Rate: ')
s_rate = switch_comas(inp)
try: reg_rate = float(s_rate)
except: warn_and_exit()

if total_hours > 40:
    extra_hours = total_hours - 40
    extra_rate = reg_rate * 1.5
    pay = 40 * reg_rate + extra_hours * extra_rate

else:
    pay = total_hours * reg_rate

print('Pay:', round(pay, 2))
