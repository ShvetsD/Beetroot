q = input('What\'s the result of 3*4?: ')
q = float(q)
while True:
    if q < 12:
        q = input('Well, you do great but try again!: ')
        q = float(q)
    elif q > 12:
        q = input('Nice effort, try more and you will succeed!: ')
        q = float(q)
    elif q == 12:
        print('Well done!')
        break
