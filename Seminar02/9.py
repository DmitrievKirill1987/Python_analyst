# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * ... * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
N = int(input('Введите число: '))
factorial = 1
A = 1
while factorial <= N:
    A = A * factorial
    factorial += 1

print(f"Факториал {N} равен {A}")

   