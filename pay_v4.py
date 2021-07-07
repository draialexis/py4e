def warn_and_exit():
    print('Error, please enter numeric input')
    quit()

def switch_comas(inp):
    coma_pos = inp.find(',')
    if not coma_pos == -1:
        inp = inp.replace(',', '.')
    return inp

def compute_pay(h, r):
    pay = 0
    if h > 40:
        extra_h = h - 40
        extra_r = r * 1.5
        pay = 40 * r + extra_h * extra_r
    else:
        pay = h * r
    return pay

inp = input('Enter Hours: ')
s_hours = switch_comas(inp)
try: total_hours = float(s_hours)
except: warn_and_exit()

inp = input('Enter Rate: ')
s_rate = switch_comas(inp)
try: reg_rate = float(s_rate)
except: warn_and_exit()

pay = compute_pay(total_hours, reg_rate)

print('Pay:', round(pay, 2))
