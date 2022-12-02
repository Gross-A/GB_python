# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# ******************* Decicion:
# from math import fsum

# def summ_of_elem():
#     lst = input('input list: ').split(',')
#     summ = fsum([int(lst[i]) for i in range(len(lst)) if i % 2 != 0])
#     print('сумма нечетных элементов списка: ', summ)

# summ_of_elem()
# ******************************************

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# ******************* Decicion:

# lst = [2, 3, 4, 5, 6]
# lst = [2, 3, 5, 6]
# def multipl_items():
#     lst = input('input list: ').split(',')
#     res_lst = [int(lst[i]) * int(lst[-(i + 1)]) for i in range(round(len(lst)/2 + 0.1))]

#     print(res_lst)


# multipl_items()

# *******************************


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# ******************* Decicion:
import math

def max_min():
    lst = input('input number: ').split(',')
    new_lst = []
    for i in lst:
        new_lst.append(float(i) - int(float(i)))

    print(new_lst)
    print(max(new_lst) - min(new_lst))


max_min()



#4.  Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# ******************* Decicion:
# import math

# def to_binary():
#     num = int(input('input number: '))
#     result = []
#     max_iter = int(math.log2(num))
#     for i in range(max_iter, 0 - 1, -1):
#         if 2**i <= num:
#             result.append(1)
#             num -= 2**i
#         else:
#             result.append(0)
#     print(''.join(map(str, result)))

# to_binary()

# *****************************************

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# ******************* Decicion:


def generator_fibonachi():
    k = int(input('введите число элементов списка: '))
    right_part_lst = [0, 1]
    left_part_lst = []

    for i in range(1, k ):
        right_part_lst.append(int(right_part_lst[i]) + int(right_part_lst[i - 1]))

    for i in range(1, k + 1 ):
        if i % 2 == 0:
            left_part_lst.append(- right_part_lst[i])
        else:
            left_part_lst.append(right_part_lst[i])

    left_part_lst.reverse()

    # print(left_part_lst)
    print(left_part_lst + right_part_lst)


generator_fibonachi()

# **************************************
