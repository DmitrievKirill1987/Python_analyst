# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы. 


def rec_sum(A, B):
    if A == 0: return B 
    else: return rec_sum(A - 1, B + 1)

A = int(input('Введите первое число: '))
B = int(input('Введите второе число: '))
print(rec_sum(A, B))
