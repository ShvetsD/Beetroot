def oops():
    try:
        raise IndexError()
    except IndexError:
        print('Index error in oops() function')
        raise

#  oops()
def call_oops():
    try:
        oops()
    except IndexError:
        print('Index error withing the call_oops() function')


call_oops()
'''If I change oops() function to raise a KeyError function will
call one and program will be terminated
'''