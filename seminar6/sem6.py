# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
def check():
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            print(list1[i], end = " ")


# n, m = int(input("Введите кол- во элементов 1: ")), int(input("Введите кол- во элементов 2: "))
# list1 = []
# list2 = []
# for i in range(n):
#     list1.append(int(input("Введите число 1 списка -> ")))
# for j in range(m):
#     list2.append(int(input("Введите число 2 списка -> ")))

# check()





# Дан массив, состоящий из целых чисел. Напишите программу, 
# которая в данном массиве определит количество элементов, у которых два соседних 
# и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество 
# элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# n = int(input("Введите кол-во элементов в массиве -> "))
# list1 = [int(i) for i in input("Введите число: ").split()]
# print(*list1)

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

# 1 2 1 2    - 2 пары
# 1 2 1 2 1   - 1+1+1+1 = 4


# n = int(input("Введите кол-во элементов в массиве -> "))
# list1 = [int(i) for i in input("Введите число: ").split()] 
# count = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         if list1[i] == list1[j]:
#             count += 1
# print(count)


# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n 
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 10^5. 
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# 300
# 220 284