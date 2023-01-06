

import user
import in_json
import json_in_list as j_i_lst

users_list = []

def create_admin():
    admin = user.create_user()
    user.add_user_in_list(admin, users_list)
    user.add_in_json(users_list, 'users.json')

# answer = 'д'

def admin_menu():
    answer = 'д'
    quest = input('Выберите действие:\n1 - вывести список пользвоателей на экран\n2 - добавить пользователя\n3 - изменить учетные данные пользователя\n4 - удалить пользователя\n0 - выйти.\nВаш выбор: ')
    
    match quest:
        case '0':
            pass
        case '1':
            show_user_info()
        case '2':
            while answer == 'д':
                add_user()
                answer = input('Ввести еще одного пользователя? (д/н): ')
        case '3':
            pass
        case '4':
            pass
        case '0':
            pass 


def add_user():

    users_list = j_i_lst.json_in_lst('users.json')
    person = user.create_user()
    user.add_user_in_list(person, users_list)
    in_json.add_in_json(users_list, 'users.json')


# ****************преобразовать json в список

def delete_user():
    users_list = user.json_in_lst('users.json')


def show_user_info():
    staff_list = j_i_lst.json_in_lst('users.json')

    person_id = 1

    for i in staff_list:
        person_name = i['name']
        person_department = i['department']
        person_job_title = i['job_title']
        # person = [person_id, i['name'], i['department'], i['job_title']]
        print(f'№: {person_id}, Имя сотрудника: {person_name}, Подразделение: {person_department}, Должность: {person_job_title}')
        person_id +=1
    



