# function to present a call-by-value argument


def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)

# function to present a call-by-reference argument


def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)
