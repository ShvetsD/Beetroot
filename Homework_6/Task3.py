from pprint import pprint
init_list = []
for i in range(1, 101):
    init_list.append(i)
pprint(f'Iitial list is: {init_list}')
a = 0
fin_list = []
while a < 100:
    if init_list[a] % 7 == 0 and init_list[a] % 5 != 0:
        fin_list.append(init_list[a])
    a += 1
print(f'Modified list is: {fin_list}')