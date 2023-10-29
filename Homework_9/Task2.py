import sys

print(dir(sys))
print('---'*10)
print(sys.path)
sys.path.append('C:\\Users\\admin\\PycharmProjects\\PY_116\\Homework_9.1')
print(sys.path)
print('---'*10)
sys.path.remove('C:\\Users\\admin\\PycharmProjects\\PY_116\\Homework_9.1')
print(sys.path)
print('---'*10)
sys.path.remove('C:\\Program Files\\JetBrains\\PyCharm 2023.2.1\\plugins\\python\\helpers\\pycharm_matplotlib_backend')
print(sys.path)
print('---'*10)
sys.path.append('C:\\Program Files\\JetBrains\\PyCharm 2023.2.1\\plugins\\python\\helpers\\pycharm_matplotlib_backend')
print(sys.path)
print('---'*10)
sys.path = []
print(sys.path)
