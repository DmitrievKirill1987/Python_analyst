# Задача 18: Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X 

N = int(input('Длина массива: '))
N_list = list()
for i in range(N):
    N_list.append(int(input(f"Введите {i+1} элемент массива: ")))

X = int(input('Введите искомое число: '))
min_diff = 1000
min_N = 0
for i in range(len(N_list)):
    if abs(N_list[i]-X) < min_diff:
        min_diff = abs(N_list[i]-X)
        min_N = N_list[i]
print(f'Самый близкий по величине элемент к заданному числу {X}: {min_N}')



