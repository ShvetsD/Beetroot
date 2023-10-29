from mymod import count_lines
from mymod import count_chars


def test(filename):
    count_chars()
    print(f'The characters quantity in the file is: {count_chars()}')
    count_lines()
    print(f'The lines quantity in the file is: {count_lines()}')
    return count_lines(), count_chars()
