weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(f'Initial list: {weekdays}', type(weekdays),)
dict1 = {i+1: weekdays[i] for i in range(0, 7)}
print(f'First dictionary: {dict1}')
dict2 = {v: k for k, v in dict1.items()}
print(f'Modified dictionary: {dict2}')
