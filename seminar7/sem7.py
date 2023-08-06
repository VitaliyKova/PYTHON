# 1) Дан список, вывести в отдельном списке буквы, а в другом цифры, используя фильтр.

# ["asd", 1, 2, "gfd"]
# ["asd", "gfd"][1,2]

# list_1 = ["asd", 1, 2, "gfd"]
# print(list(filter(lambda x: type(x) == str, list_1 )))
# print(list(filter(lambda x: type(x) == int, list_1 )))

# 2) Дано вещественное число, показать сумму его цифр.

# num = 3.12
# stroka = str(num)

# res = list(filter(lambda x: x != ".", stroka))
# res = sum(list(map(int, res)))

# print(res)




# Дан список чиселБ нужно вывести двухзначные

# list_1 = [1, 20, 3, 40, 555, 6, 10, 99, 100]

# print(list(filter(lambda x: 10 <= x < 100, list_1)))


# У вас есть код, который вы не можете менять(так часто бывает, когда код в 
# глубине программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать 
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.


# ```python
# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
# 	print('ok')
# else:
# 	print('fail')
# ```