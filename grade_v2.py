err_msg = 'Bad score'
def computegrade(inp):
    try:
        score = float(inp)
    except:
        print(err_msg)
        quit()
    if score > 1.0 or score < 0.0:
        print(err_msg)
    elif score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else: print('F')

computegrade(input('Enter a score between 0.0 and 1.0: '))
