a = input('Please type or paste  your sentence here: ')
a = a.lower()
a = a.replace('.', '')
a = a.replace(',', '')
a = a.replace('!', '')
a = a.replace('?', '')
a = list(a.split())
print(f'Initial list is: {a}')
b = set(a)
print(f'Final list is: {a}')
dict_a = {}
for i in b:
    dict_a[i] = a.count(i)
print(f'{dict_a=}')
