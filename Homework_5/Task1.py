import random
print('Let\'s play some guessing game?')
number = int(input('Guess number from 1 to 10?: '))
while True:
    computer = random.randint(1, 10)
    if number < 1 or number > 10:
        print('Please be attentive and type number within range from 1 to 10')
        number = int(input('Gues number form 1 to 10?: '))
    elif number != computer:
        print('Try again!')
        number = int(input('Gues number form 1 to 10?: '))
    else:
        print('Well done! ')
        break
