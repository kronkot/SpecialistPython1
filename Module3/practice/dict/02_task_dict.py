# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.

keys = ['name', 'surname', 'age', 'rate']
values = ['Петр', 'Первый', 42, 1300]

# TODO: your code here
# Нужно получить словарь:
# {'name': 'Петр', 'surname': 'Первый', 'age': 42, 'rate': 1300}


keys = ['name', 'surname', 'age', 'rate']
values = ['Петр', 'Перый', 42, 1300]

dict1 = {}
for i in range(len(keys)):
    dict1[keys[i]] = values[i]
print(dict1)

#print(list(range(1,6,2)))
