import random
word = input('Please enter any word: ')
#  Create a list from the string(as input is always a string)
#  in order to get the output as in task(not sure if necessary)
word_l = list(word)
print(word_l, end=' ')  # Input as the list presentation
print('->', end=' ')  # Just to print arrow
a = 0
while a < 5:
    words = ''.join(random.sample(word, len(word)))  # Transform list back to the string
    print(words, end=', ')
    a += 1
