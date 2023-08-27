from interfeys import *

start = 0

def menu_func(start):
    if start == 1:
        from work_file import add_contact
        strok = stroka()
        add_contact('tel_book.txt', strok)
    elif start == 2:
        from work_file import print_conatact
        print_conatact('tel_book.txt')
    elif start == 3:
        from work_file import search_username
        nam = name()
        search_username('tel_book.txt', nam)
    elif start == 4:
        from work_file import replace_name
        old_nam = old_name()
        new_nam = new_name()
        replace_name('tel_book.txt', old_nam, new_nam)
    elif start == 5:
        from work_file import delete_name
        del_name = deleted_name()
        delete_name('tel_book.txt', del_name)    


while start != 6:
    print()
    start = print_menu()
    menu_func(start)