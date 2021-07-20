def chop(t):
    del t[len(t)-1]
    del t[0]

my_list = [1, 'e', [4, True], 4.03, False]
chop(my_list)
print(my_list)
