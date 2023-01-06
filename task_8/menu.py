import user
import administrator
import checker
import json_in_list


lst = json_in_list.json_in_lst('users.json')

# при первом входе система только предлагает создать пользователей

def login_first_time():
# while output == False:
    if checker.check_json(): # если файл users.json пуст, то ...
        print('В системе еще нет пользователей. Введите учетные данные администратора системы: ')
        administrator.create_admin()
        empty = False

        question = input('Желаете зарегистрировать пользователя в системе? (д/н): ')

        while question == 'д':
            administrator.add_user()
            question = ('Желаете зарегистрировать пользователя в системе? (д/н): ')
        
        if question == 'н':
            administrator.admin_menu()
    else:
        pass




def login():

    if not checker.check_json(): # если в файле users.json есть записи, то ...
        print('Для входа в систему введите логин и пароль.')
        # log = input('Введите логин: ')
        # passw = input('Введите пароль: ')

        check_log, user_name, department = checker.check_log_passw()

        match check_log:
            case '0':
                administrator.admin_menu()

                output = True
            
            case '1':
                user.show_manager_menu(department)
                output = True

            case '2':
                user.show_employee_menu(user_name)
                output = True
    else:
        pass

