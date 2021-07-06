def warn_and_exit():
    print('Error, please enter numeric input')
    quit()

s_hours = input('Enter Hours: ')
try: total_hours = float(s_hours)
except: warn_and_exit()

s_rate = input('Enter Rate: ')
try: reg_rate = float(s_rate)
except: warn_and_exit()

if total_hours > 40:
    extra_hours = total_hours - 40
    extra_rate = reg_rate * 1.5
    pay = 40 * reg_rate + extra_hours * extra_rate

else:
    pay = total_hours * reg_rate

print('Pay:', round(pay, 2))
