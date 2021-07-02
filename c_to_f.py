choice = input("Type 'c' to convert from 'Celsius' or 'f' to convert from 'Farenheit': ")
if choice == 'c':
    c_temp = float(input('Enter a temperature in Celsius: '))
    f_temp = c_temp * 9 / 5 + 32
    print(f_temp)

elif choice == 'f':
    f_temp = float(input('Enter a temperature in Celsius: '))
    c_temp = (f_temp - 32) * 5 / 9
    print(c_temp)

else:
    print('Invalid input -- please choose the conversion you want')
