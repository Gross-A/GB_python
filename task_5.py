# 1 Напишите программу, удаляющую из файла все слова, содержащие "абв".

 
# *************************************** work variant*********************
# with open('test.txt', 'r') as data:
#     str_1 = data.read()
# # print(str_1.split(' '))
# """новая строка для записи в файл: искомая строка преобразуется в список элементов, 
#    разделенных пробелом str_1.split(' '), далее с помощью лямбда перебираем каждый элемент (слово)
#    проверяем на наличие "абв" через find. если x.find('абв') == -1 истинно, то элемент остается в резуль
#    тирующем списке.
#    Далее объект filter() преобразуем в список. Асписок через join()  в строку.
#    получившуюся строку записываем в файл.
# """

# str_new = ' '.join(list(filter(lambda x: x.find('абв') == -1, str_1.split(' '))))

# with open('test_1.txt', 'w') as data:
#     data.write(str_new)

# **************************************finish******************



# .
# .
# 2 Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# **************************Descition***************

'''жеребьевка'''
def lotery():
    players = input('введите имена игроков через запятую: ').split()
    import random
    num = random.randint(0, 10)
    '''print(num)'''
    if num >= 6:
        print(f'превым ходит игрок {players[1]}')
    else:
        print(f'превым ходит игрок {players[0]}')


# #************************** игра против бота**************
vs = ''
def vs_comp():
    vs = input('выберите режим игры: введите "1" - 2 игрока, введите "2" - игра против бота.::')

    if vs == '1':
        lotery()
    return vs

vs = vs_comp()
'''print(vs, type(vs))'''
num = 2021
sweet_p1 = 0
sweet_p2 = 0



# '''пока количесвто конфет не уменшилось до значения 85 каждый игрок выбирает по одной конфете
# попеременно (нужно добавить еще функцию кто первый начинает игрок один или два). 
# после того как очередной цикл взятия конфет заканчивается общим числом оставшихся меньше 85, то
# программа анализирует сколько нужно взять игроку один, чтоб после игрока два остались
#  конфеты в любом случае'''

import random
while num >= 85:
    num_play_1 = int(input('Игрок 1 введите число конфет от 1 до 28: '))
    num = num - num_play_1
    sweet_p1 += num_play_1
    move = 'play_1'
    num_play_2 = 0
    if vs == '1':
        num_play_2 = int(input('Игрок 2 введите число конфет от 1 до 28: '))
    else:
        num_play_2 = random.randint(1, 28)
        print(f'бот берет {num_play_2} конфет')

    num = num - num_play_2
    sweet_p2 += num_play_2

    move = 'play_2'
    print('количество оставшихся конфет', num)

'''print('p1: ', sweet_p1, 'p2: ', sweet_p2)'''
if (num > 56):
    num_play_1 = int(input(f'рекомендуем первому игроку взять {num - 56} конфет'))
    if vs == '1':
        num_play_2 = int(input('Игрок 2 введите число конфет от 1 до 28: '))
    else:
        num_play_2 = random.randint(1, 28)
        print(f'бот берет {num_play_2} конфет')

else:
    num_play_1 = int(input(f'рекомендуем первому игроку взять {num - 29} конфет'))
    if vs == '1':
        num_play_2 = int(input('Игрок 2 введите число конфет от 1 до 28: '))
    else:
        num_play_2 = random.randint(1, 28)
        print(f'бот берет {num_play_2} конфет')
        
num = num - num_play_1
sweet_p1 += num_play_1

'''num_play_2 = int(input('Игрок 2 введите число конфет от 1 до 28: '))'''
sweet_p2 += num_play_2


num = num - num_play_2
sweet_p1 = sweet_p1 + num
print('игра завершена. игрок один выиграл. у него {sweet_p1} конфет')


#***************************************************


# .
# 3 Создайте программу для игры в "Крестики-нолики".

# Вариант интерфейса:

#  1  |  2 | 3
# --------------
#  4  |  5 | 6
# --------------
#  7  |  8 | 9


# ****************************decicion*****************


# """создадим список выигрышных вариаций расположения "Х" или "О"
# на игровом поле. Далее """
# win = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7]]

# tic_tac = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# inp_p = ''
# lst_x = []              #список выбранных полей игрока "х"
# lst_o = []              #список выбранных полей игрока "о"

# """функция для записи выполненных ходов обоих игроков в файле отображения хода игры"""

# def write_res(text):
#     with open('tic_tac_toe_res.txt', 'w') as file:
#         file.write(text)


# """функция для запроса номера ячейки игрового поля, которую игрок хочет занять"""

# def input_mean(el):
#     return int(input(f'введите номер поля для установки {el}: '))


# """функция для присвоения выбранной ячейке значения х или о и запись хода в файл отображения хода игры"""

# def set_elem(el, player_lst):
#     inp_p = input_mean(el)
#     player_lst.append(inp_p)
#     for i in range(len(tic_tac)):       #цикл в списке tic-tac
#         if tic_tac[i] == inp_p:
#             tic_tac[i] = el
#             # print('after set_elem: ', tic_tac)

#     file_txt = f' {tic_tac[0]} | {tic_tac[1]} | {tic_tac[2]} \n {tic_tac[3]} | {tic_tac[4]} | {tic_tac[5]} \n {tic_tac[6]} | {tic_tac[7]} | {tic_tac[8]}'

#     write_res(file_txt)
# """file_txt - форма записи данных в файл отображения хода игры"""




# """циклы запроса у игроков ячеек продолжаются пока "флаг" не примет значение 'game over'"""
# def start_game():
#     count = 0               #счет сделанных ходов
#     stop_game = ''          #"флаг" для остановки игры в случае выигрыша

#     start = input('are you ready? (y or n)')
#     if start == 'y':
#         while stop_game != 'game over':
#             p =''
#             if count % 2 == 0:          # переход хода между игрокамию если count - четное, то ходит игрок х
#                 p = 'X'
#                 player_lst = lst_x      #список, куда добавляется номер выбранной ячейки игрового поля
                
#             else:
#                 p = 'O'
#                 player_lst = lst_o

#             set_elem(p, player_lst)     #вызов функции присвоения значения ячейке с аргументами: игрок и список, куда записывается номер ячейки
#             count += 1
#             """если счет больше 4, то начинаем проверять списки выбранных номеров выбранных ячеек игроков
#             на совпадение с выигрышными комбинациями"""
#             if count > 4:
#                 player_lst.sort()
#                 for i in win:
#                     if i == player_lst:
#                         print(f'победа игрока {p}')
#                         stop_game = 'game over'


# start_game()
# *****************************************finish***************
# .
# .

# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

# aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
# 4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff

# *********************************Decicion***************

# str = 'aaaasssdddwwwwwwwwwwwweeeffffff'
# lst = list(str)
# res_lst = []
# # print(lst, 'lst')
# res_count = 0
# count = 1

# for i in range(len(lst) - 1):
#     if lst[i] == lst[i + 1] and i != len(lst) - 2:
#         count += 1
#         # print(count)
#     elif lst[i] == lst[(len(lst) - 1)]:
#         res_count += count
#         str_res = f'{count}{lst[i]}'
#         res_lst.append(str_res)
#         break
#     else:
#         res_count += count
#         res_str = ''
#         if count > 9:
#             str_res = f'9{lst[i]}{count - 9}{lst[i]}'

#         else:
#             str_res = f'{count}{lst[i]}'
#         res_lst.append(str_res)
#         count = 1
#         continue

# print(res_lst)

# res_str = ''.join(res_lst)
# # print(res_str)
# import re
# decod_lst = re.findall(r'\d+\w', res_str)
# fin_lst = []
# for item in decod_lst:
#     fin_item = item[1] * int(item[0])
#     fin_lst.append(fin_item)

# print(fin_lst)
# fin_str = ''.join(fin_lst)
# print(fin_str)



# *********************************************

# .
# .
# 5* Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.

# *Пример:* 

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

