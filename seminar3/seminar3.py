# spisok = list()
# slovar = dict()
# mnoj = set()
# mnoj.add(3)
# spisok = [i for i in input().split()] 


# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# list_1 = [1,1,3,5,7,89]
# mnoj = set(list_1)
# print(mnoj)
# print(len(mnoj))


# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю 
# последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

# spisok = [1,2,3,4,5,6,7]
# k = int(input("Введите значение"))
# spisok = spisok[len(spisok) - k :] + spisok[:len(spisok) - k]
# print(spisok)



# Напишите программу для печати всех уникальных значений в словаре.
# {1:"один",                                          }

# slovar = {1: "привет", 2: "phyton", 3: "plus", 4: "plus", 5: "phyton"}
# print(set(slovar.values()))


# Дан массив, состоящий из целых чисел. Напишите программу, 
# которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)

# spisok = [1,1,1,2,4,6,8,1,1,2]
# count = 0
# min_value = spisok[0]
# for i in spisok:
#     if i > min_value: count += 1
#         # count += 1
#     min_value = i
# print(count)        


