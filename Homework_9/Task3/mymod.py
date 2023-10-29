import sys

path = 'Song_lyrics.txt'


def count_lines():
    with open(path, 'r') as opened_file:
        a = opened_file.readlines()
        b = len(a)
    return b


def count_chars():
    with open(path, 'r') as opened_file:
        c = opened_file.read()
        # c = c.replace(' ', '').replace('?', '').replace('"', '').replace(',', '')
        # f = opened_file.seek(0, 1)
        f = len(c)
    return f


#  print(count_chars())
def test(filename):
    d = count_lines()
    print(f'The lines quantity in the file is: {d}')
    e = count_chars()
    print(f'The characters quantity in the file is: {e}')
    return d, e


test(path)

print(sys.path)