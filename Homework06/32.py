# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного
# максимума)

def int_input(text):
    return int(input(text))

def create_list():
    result_list = []
    for i in range(int(input(f'Введите длину списка: '))):
        result_list.append(int(input(f'Введите {i+1} элемент списка: ')))
    return result_list

def find_index(some_list, some_min, some_max):
    result_list = []
    for i in range(len(some_list)):
        if some_min < some_list[i] < some_max: result_list.append(i)
    return result_list

my_list = create_list()
my_min = int_input('Введите минимальное значение: ')
my_max = int_input('Введите максимальное значение: ')
print(find_index(my_list, my_min, my_max))