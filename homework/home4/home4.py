# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# n, m = int(input("Введите кол - во элементов в первом множестве -> ")), int(input("Введите кол - во элементов во втором множестве -> "))
# mn1 = set()
# mn2 = set()
# for i in range(n):
#     mn1.add(int(input(f"Введите {i + 1}-й элемент в множестве 1 -> ")))
# for i in range(m):
#     mn2.add(int(input(f"Введите {i + 1}-й элемент в множестве 2 -> ")))

    
# union_mn = mn1.intersection(mn2)
# print(*sorted(union_mn))

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# 3 1 2 4


# list_1 = [14, 1, 2, 4]
# summa = []
# i = 0
# while i < len(list_1):
#     if i == 0:
#         summa.append(list_1[0] + list_1[1] + list_1[-1])
#     elif i == len(list_1) - 1:
#         summa.append(list_1[len(list_1) - 1] + list_1[len(list_1) - 2] + list_1[0])
#     else:
#         summa.append(list_1[i] + list_1[i - 1] + list_1[i + 1])
#     i += 1         

# print(f" Максимальное кол-во ягод -> {max(summa)} при у становке на куст № {summa.index(max(summa))}")