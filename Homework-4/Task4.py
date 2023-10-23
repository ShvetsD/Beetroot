name = 'denys'
check_name = input('Please enter your name: ')
check_name = check_name.lower()
while True:
    if check_name == name:
        print('You\'ve entered correct name, thank you!')
        break
    else:
        print('You\'ve entered the wrong name, please try again: ')
        check_name = input('Please enter your name: ')
        check_name = check_name.lower()
