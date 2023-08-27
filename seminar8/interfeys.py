# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по фамилии
# 4 - выход
# 5 - Редактирование контакта
# 6 - Удаление контакта

def print_menu():
    print('1 - Добавление контакта \n 2 - Вывод всех \n 3 - Поиск по фамилии \n 4 - Редактирование контакта \n 5 - Удаление контакта \n 6 - Выход')
    start = int(input("Выберите действие -> "))
    print()
    return start

def stroka():
    stroka = input("Введите ФИО и номер телефона через пробел -> ")
    return stroka

def name():
    name = input("Введите искомую фамилию -> ")
    return name

def old_name():
    old_name = input("Введите фамилию контакта, данные которого хотите изменить -> ")
    return old_name

def new_name():
    new_name = input("Введите новые данные контакта -> ")
    return new_name

def deleted_name():
    delet_name = input("Введите фамилию, которую хотите удалить -> ")
    return delet_name
            





            
