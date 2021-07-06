s_hours = input('Enter Hours: ')
s_rate = input('Enter Rate: ')
total_hours = float(s_hours)
reg_rate = float(s_rate)

if total_hours > 40:
    extra_hours = total_hours - 40
    extra_rate = reg_rate * 1.5
    pay = 40 * reg_rate + extra_hours * extra_rate

else:
    pay = total_hours * reg_rate
    
print('Pay:', round(pay, 2))
