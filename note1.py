print('Hello, world!')
try:
    prnity('Hello, world!')
except NameError:
    pass
a = [1, 2, 2]
help = dir(a)
print(help)
# python3 -m trace --trace *.py
