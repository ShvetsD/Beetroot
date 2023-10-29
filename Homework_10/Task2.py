

def task2_func():
    while True:
        try:
            a = int(input('Please enter the first value: '))
            b = int(input('Please enter the second value: '))
            c = a ** 2 / b
        except ValueError:
            print('Entered values should be integers')
            continue
        except ZeroDivisionError:
            print('Second value should differ from zero!')
            continue
        print(f'Great job, the answer is: {c}')
        return c


task2_func()
