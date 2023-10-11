import random
a = 0
list1 = []
list2 = []
list3 = []
while a < 10:  # cycle to make 2 lists with 10 symbols long
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    list1.append(b)
    list2.append(c)
    a += 1
print('Randomly generated list1: ', list1)
print('Randomly generated list2: ', list2)
set1 = set(list1)
set2 = set(list2)
print(f'set1 is: {set1}')
print(f'set2 is: {set2}')
list3 = list(set1.intersection(set2))  # create a list with integers common for two lists without duplicates
print(f'Final list is: {list3}')
