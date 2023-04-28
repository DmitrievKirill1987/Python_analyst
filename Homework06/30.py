# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def int_input(text):
    return int(input(text))

def arith_progr(a1, d, n):
    progr_list = []
    for a in range(1,n+1):
        progr_list.append(a1 + d*(a-1))
    return progr_list

my_a1 = int_input('Введите первый элемент прогрессии: ')
my_d = int_input('Введите разность прогрессии: ')
my_n = int_input('Введите количество элементов: ')
print(arith_progr(my_a1,my_d,my_n))