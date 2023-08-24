from interaeys import *


def menu_func(start):
    if start == 1:
        from work_file import add_contact
        from interaeys import stroka
        strok = stroka()
        add_contact('tel_book.txt', strok)
    elif start == 2:
        from work_file import print_conatact
        print_conatact('tel_book.txt')
    elif start == 3:
        from work_file import search_username
        from interaeys import name
        nam = name()
        search_username('tel_book.txt', nam)

start = 0
while start != 4:
    print()
    start = print_menu()
    menu_func(start)