# проверка вводимых данных


import json_in_list

# проверка файл на наличие записей (логика: если он не пустой, то там есть администратор). 
# Потом нужно довести до ума с проверкой наличи в файле записи со статусом админ


def check_json():
    lst = json_in_list.json_in_lst('users.json')

    if len(lst) > 0:
        return False
    else:
        return True

#  проверка на правильность введенных логина и пароля
# после ввода логина и пароля данные проверяются с элементами списка json
# если есть совпадение, то возвращается значение ключа user_status для определения 
# статуса пользователя, вошедшего в систему (админ, руководитель или работник)


def check_log_passw():
    lst = json_in_list.json_in_lst('users.json')
    # print(lst, len(lst))
    log = input('Введите логин: ')
    passw = input('Введите пароль: ')
    consilience = False # совпадение
    # print(lst[1]['log'],log, lst[1]['passw'], passw)

    for i in lst:
        # print(i, i['log'],log, i['passw'], passw)

        if (i['log'] == log) and (i['passw'] == passw):
            user_stat = i['user_status']
            user_name = i['name']
            department = i['department']
            # print('корректный ввод')
            consilience = True
            # return user_stat
    
    if consilience:
        print('корректный ввод')
        
        print(user_stat)
        return user_stat, user_name, department


    else:
        ask = input('допущена ошибка при вводе. Попробуйте еще раз. (д/н): ')
        if ask == 'д':
            check_log_passw()
        else:
            pass


# check_log_passw()