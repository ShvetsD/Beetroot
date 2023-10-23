q = input('Please enter the phone number: ')
while len(q) != 10:
    if q.isdigit():
        if len(q) < 10:
            q = input('Entered number is too short, please enter the correct number: ')
        elif len(q) > 10:
            q = input('Entered number is too long, please enter the correct number: ')
    else:
        q = input('Number should contain only digits, please enter the correct number: ')

print('Thank you, entry is correct')
