def rect_volume(x):
    def rect_area():
        a = abs(x - 4) * abs(x - 6) * x
        if a == 0:
            print('Please try another \'x\'')

        return a

    return rect_area()


print(rect_volume(8))
