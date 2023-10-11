import random
a = 0
list1 = []
while a < 10:
    b = random.randint(1, 10)
    list1.append(b)
    a += 1
print('Randomly generated list1: ', list1)
print(max(list1))
