# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

a = int(input('Введите число журавликов, которые сделали дети: '))
b = round(a/6)
c = round(b*4)
print(f'У Пети и Сережи по: {b} шт., а у Кати: {c} шт.')