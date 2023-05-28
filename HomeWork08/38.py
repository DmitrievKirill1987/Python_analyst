# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных

import os
import shutil
import Functions

os.chdir('C:/Users/User/Desktop/Python_analyst/Homework08')

Functions.info_func()
while (user_action:=int(input('Выберите действие (1,2,3 и т.д.): '))) != 6:
    match user_action:
        case 1: Functions.print_records()
        case 2: Functions.add_record()
        case 3: Functions.find_record()
        case 4: Functions.change_record()
        case 5: Functions.delete_record()
        case 6: pass
        case _: print('Нет такого действия.')