def make_operation(a, b, *args):
    sum1 = b
    ded1 = b
    mult1 = b
    if a == '+':
        for i in args:
            sum1 += i
        return sum1
    elif a == '-':
        for i in args:
            ded1 -= i
        return ded1
    elif a == '*':
        for i in args:
            mult1 *= i
        return mult1


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
