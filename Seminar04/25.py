# Принимаем строку и считаем количество поворяющихся букв букв
# добавляя .split.('a a a b c a a d c d d')

test_list = (input('-->')).split()
slovar = {}
for letter in test_list:
    if letter in slovar:
        print(f'{letter}_{slovar[letter]}', end=' ')
        slovar[letter] += 1
    else:
        print(f'{letter}', end= ' ')
        slovar[letter]=1 






