# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым

def prime_number(x):
    counter = 0
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            counter += 1
        return False
    return True
print(prime_number)
