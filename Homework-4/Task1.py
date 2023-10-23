# Sample string is helloworld
string = "helloworld"
print(string[:2]+string[-2:])
# Sample string is my
string = "my"
print(string[:2]+string[-2:])
# Sample string is x
string = "x"
if len(string) < 2:
    print("Empty String")
else:
    print(string[:2]+string[-2:])
