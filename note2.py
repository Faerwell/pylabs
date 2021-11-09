# Заменить все х на у
init_list = ['x', 'xx', 'xxx']
new_list = []
for x in init_list:
    new_list.append(x.replace('x', 'y'))

print(new_list)

# Сосчитать произведение чисел, кратных 3 и 5
num = int(input('input num:'))
x, y = 0, 0
for i in range(num):
    if i % 3 == 0:
        x = i
    if i % 5 == 0:
        y = i
print(x, '*', y, '=', x * y)

