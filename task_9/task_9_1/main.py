
# ****************************decicion*****************

import emoji


# функция выбора эмоджи для хода игрока 
def choose_sign(number_of_player):
      
    emojis = [':Belarus:', ':OK_hand:', ':Russia:', ':Santa_Claus:',
                ':baby:', ':beaming_face_with_smiling_eyes:', ':bear:',
                ':cross_mark:', ':cyclone:', ':doughnut:']

    for count, value in enumerate(emojis, start=1):
        print (f'{count} - {emoji.emojize(value)}')
    
    player_num = int(input(f'Выберите номер аватара для игрока {number_of_player}: '))
    player_emoji = emoji.emojize(emojis[player_num - 1])

    return player_emoji

########choose_sign()

"""создадим список выигрышных вариаций расположения "Х" или "О"
на игровом поле. Далее """
win = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7]]

tic_tac = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# emojis = [':Belarus:', ':OK_hand:', ':Russia:', ':Santa_Claus:',
#             ':baby:', ':beaming_face_with_smiling_eyes:']

# for i in emoji:
#     print (i, emoji.emojize(i))


inp_p = ''
lst_x = []              #список выбранных полей игрока "х"
lst_o = []              #список выбранных полей игрока "о"

"""функция для записи выполненных ходов обоих игроков в файле отображения хода игры"""

def write_res(text):
    with open('tic_tac_toe_res.txt', 'w') as file:
        file.write(text)


"""функция для запроса номера ячейки игрового поля, которую игрок хочет занять"""

def input_mean(el):
    return int(input(f'введите номер поля для установки {el}: '))


"""функция для присвоения выбранной ячейке значения х или о и запись хода в файл отображения хода игры"""

def set_elem(el, player_lst):
    inp_p = input_mean(el)
    player_lst.append(inp_p)
    for i in range(len(tic_tac)):       #цикл в списке tic-tac
        if tic_tac[i] == inp_p:
            tic_tac[i] = el
            # print('after set_elem: ', tic_tac)

    file_txt = f' {tic_tac[0]} | {tic_tac[1]} | {tic_tac[2]} \n {tic_tac[3]} | {tic_tac[4]} | {tic_tac[5]} \n {tic_tac[6]} | {tic_tac[7]} | {tic_tac[8]}'

    write_res(file_txt)
"""file_txt - форма записи данных в файл отображения хода игры"""




"""циклы запроса у игроков ячеек продолжаются пока "флаг" не примет значение 'game over'"""
def start_game():
    count = 0               #счет сделанных ходов
    stop_game = ''          #"флаг" для остановки игры в случае выигрыша
    player_1 = choose_sign(1) 
    player_2 = choose_sign(2)
    start = input('are you ready? (y/n): ')
    if start == 'y':
        while stop_game != 'game over':
            p =''
            if count % 2 == 0:          # переход хода между игрокамию если count - четное, то ходит игрок х
                p = player_1
                player_lst = lst_x      #список, куда добавляется номер выбранной ячейки игрового поля
                
            else:
                p = player_2
                player_lst = lst_o

            set_elem(p, player_lst)     #вызов функции присвоения значения ячейке с аргументами: игрок и список, куда записывается номер ячейки
            count += 1
            """если счет больше 4, то начинаем проверять списки выбранных номеров выбранных ячеек игроков
            на совпадение с выигрышными комбинациями"""
            if count > 4:
                player_lst.sort()
                for i in win:
                    if i == player_lst:
                        print(f'победа игрока {p}')
                        stop_game = 'game over'


start_game()
