def count_local():
    var1 = 0
    b = 7
    str1 = 'Hello out there'
    print('The number of local variables is: ', count_local.__code__.co_nlocals)

count_local()