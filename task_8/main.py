'''программа для взаимодействия внутри компании: постановке задач руководителями отделов своим подчиненным,
просмотр работниками поставленных именно им задач, отчет руководителю о выполнении поставленной задачи(не успел пока реализовать)

при первом входев систему администратору предлагается создать пользователей с указанием 
имен, должностей, названий подразделения, статуса работника(руководитель, исполнитель),
задать пользователю логин и пароль.

при входе в систему зарегистрированного пользователя со статусом "руководитель"
появляется меню с выбором действий руководителя (посмотреть список сотрудников его подразделения,
посмтавить задачу определенному сотруднику).

при входе в систему зарегистрированного пользователя со статусом "исполнитель"
появляется меню с выбором действий испонителя (посмотреть список поставленных ему задач, 
подтвердить факт выполнения (не доделал) 

все данные о регистрируемых администратором сотрудниках хранятся в файле users.json
все данные о выданных заданиях храняться в файле tasks.json
 '''


import menu

menu.login_first_time()

menu.login()


# import user
# import administrator
# import checker
# import json_in_list

# empty = True

# output = False

# lst = json_in_list.json_in_lst('users.json')

# # при первом входе система только предлагает создать пользователей

# while output == False:
#     if checker.check_json(): # если файл users.json пуст, то ...
#         print('В системе еще нет пользователей. Введите учетные данные администратора системы: ')
#         administrator.create_admin()
#         empty = False

#         question = input('Желаете зарегистрировать пользователя в системе? (д/н): ')

#         while question == 'д':
#             administrator.add_user()
#             question = ('Желаете зарегистрировать пользователя в системе? (д/н): ')
        
#         if question == 'н':
#             administrator.admin_menu()




#     else: # если в файле users.json есть записи, то ...
#         print('Для входа в систему введите логин и пароль.')
#         # log = input('Введите логин: ')
#         # passw = input('Введите пароль: ')

#         check_log, user_name, department = checker.check_log_passw()


#         if  check_log == '0':
#             administrator.admin_menu()

#             output = True
        
#         elif check_log == '1':
#             user.show_manager_menu(department)
#             output = True

#         elif check_log == '2':
#             user.show_employee_menu(user_name)
#             output = True













