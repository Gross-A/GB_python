import checker as check
# phonebook = []
request = True



def input_person():
    global request
    phonebook = []

    while request == True:
        inp_person = input('Введите данные об абоненте в формате "Фамилия" "Имя" "Телефон(+79999999999" ')

        add = input('Желаете ввести комментарий к записи об абоненте? (д/н)')

        inp_person_inf = ''


        inp_person_lst = inp_person.split(' ')  #преобразование введенных данных в список


        if add == 'д':
            inp_person_inf = input('Введите доп информацию: ')

        inp_person_lst.append(inp_person_inf)   #добавить доп информацию об абоненте
        #преобразуем запись об абоненте из списка в кортеж для дальнейшего добавления в справочник после проверки правильности ввода данных
        # **************************************************
        # inp_person_tuple = (inp_person_lst[0], inp_person_lst[1], inp_person_lst[2], inp_person_lst[3])
        # *************************************************
        '''запускаем проверку правильности введенных в кортеж данных. обращение к модулю checker.py
        если возвращает True, то кортеж добавляется в список справочник и идет запрос на дальнейшее действие
        если False то выводится соответствующее сообщение и снова рекурсивно запускается функция input_person()'''
        # if check.check_correct(inp_person_tuple):
        if check.check_correct(inp_person_lst):

            # phonebook.append(inp_person_tuple)
            phonebook.append(inp_person_lst)

            next = input('желаете ввести следуеющего абонента?(д/н)')
            if next == 'д':
                input_person()
                request = True
            else:
                request = False
                break
        else:
            print('введены некорректные данные. Повторите ввод')
            input_person()
    return phonebook






















#*****************************************************************
# extens = 'txt'

# file_in = 'test.' + extens

# text = 'dafkhaksfhdkahflkadjflkdajskfl'

# with open(file_in, 'w') as file:
#     file.write (text)