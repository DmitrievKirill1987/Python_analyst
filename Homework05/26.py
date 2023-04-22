# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def nums(number, degree):
    if degree == 1: return number
    else: return number*nums(number, degree-1)

A = int(input('Введите первое число: '))
B = int(input('Введите второе число: '))
print(nums(A, B))

 