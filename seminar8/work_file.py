
def add_contact(file_name, spisok):
    tel = open(file_name, 'a', encoding='utf-8')
    tel.write(spisok + '\n')
    tel.close

def print_conatact(file_name):
    tel = open(file_name, 'r', encoding='utf-8')
    for line in tel:
        print(line)
    tel.close

def search_username(file_name, name):
    flag = False
    tel = open(file_name, 'r', encoding='utf-8')
    for line in tel:
        if name in line:
            print(line)
            flag = True
    if flag == False:
        print("не найдено")           
    tel.close

def replace_name(file_name, old_name, new_name):
    with open(file_name, 'r+', encoding='utf-8') as tel:
        lines = tel.readlines()
        with open(file_name, 'w+', encoding='utf-8') as tel2:
            for line in lines:
                if old_name in line:
                    line = line.replace(old_name, new_name)
                tel2.write(line)
        print("Данные успешно изменены")

def delete_name(file_name, delete_name):
    with open(file_name, 'r', encoding='utf-8') as tel:
        lines = tel.readlines()
        with open(file_name, 'w', encoding='utf-8') as tel2:
            for line in lines:
                if delete_name not in line:
                    tel2.write(line)
            print("Контакт удалён!")



