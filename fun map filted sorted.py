a = [3, 4, 5, 2, 7, 8]
b = [7, 9, 2, 4, 5, 1]
c = [5, 7, 3, 4, 5, 9]

# Это список, содержащий словари
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

# Функция map() - применяет функцию к каждому элементу итерируемого объекта(ов)
# print(list(map(lambda x, y, z: x + y + z, a, b, c)))

# print(list(map(lambda x: x['name'], dict_a)))
# Нашел ключ, достал значение, сохранил его в список

# print(list(map(lambda x: x['name'] == 'python', dict_a)))
# Проверит, равен ли ключ питону, выдаст тру или фолс

# filter - собирает и пропускает только то, 
# что дает истину в его логическом выражении

# print(list(filter(lambda x: x>5, c)))

dict_b = [{"name": "John", "age": 12},
            {"name": "Sonia", "age": 10},
            {"name": "Steven", "age": 13},
            {"name": "Natasha", "age": 9}]

names = ["Abram", "Arib", "Bob", "Shawn",
            "Aria", "Cicilia", "John", "Reema",
            "Alice", "Craig", "Aaron", "Simi"]

# sorted -  сортирует по заданному параметру все элементы итерируемого объекта
# по умолчанию сортирует по возрастанию

# отсортирует по принципу заканчивается на n
#print(sorted(names, key=lambda x: x.endswith('n')))

# Отсортирует возраст по возрастанию
# достали значение по ключу и отсортировали
print(sorted(map(lambda x: x['age'], dict_b)))

# Сортировка словарей от максимального к минимальному (reverse=True)
# относительно параметра age
print(*sorted(dict_b, key=lambda x: x['age'], reverse=True), sep='\n')