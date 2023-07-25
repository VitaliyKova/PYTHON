# 25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.



# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# input_string = input("Введите строку").split()
# dict_string = {}
# out_string = ""
# for el in input_string:
#     if el not in dict_string:
#         out_string += f"{el} "
#     else:
#         out_string += f"{el}_{dict_string[el]} "
#     dict_string[el] = dict_string.get(el, 0) + 1

# print(out_string)

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# print(len(set(input("Введите строку - > ").lower().split())))

# Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)

# list = [1, 4, 3, 0]
# max = list[0]
# index = 0
# while list[index] != 0:
#         if list[index] > max:
#             max = list[index]
#         index += 1    
# print(max)            

