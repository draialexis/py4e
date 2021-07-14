def find_and_print(str, delimitor):
    start = str.find(delimitor)
    end = None
    if not str.find(' ', start) == -1:
        end = str.find(' ', start)
    substr = str[start+1:end]
    try:
        result = float(substr)
    except:
        print('Something went wrong: cannot convert to float')
    return result

str = 'X-DSPAM-Confidence:0.8475'
print(find_and_print(str, ':'))
