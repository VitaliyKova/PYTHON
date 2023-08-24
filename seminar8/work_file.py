
def add_contact(file_name, spisok):
    tel = open(file_name, 'a')
    tel.write(spisok + '\n')
    tel.close

def print_conatact(file_name):
    tel = open(file_name, 'r')
    for line in tel:
        print(line)
    tel.close

def search_username(file_name, name):
    flag = False
    tel = open(file_name, 'r')
    for line in tel:
        if name in line:
            print(line)
            flag = True
    if flag == False:
        print("не найдено")           
    tel.close        



