

# print('Укажите какое действие вы хотите выполнить:\n1. Добавить пользователя в систему.\n2. Просмотреть всех пользователей системы.\n 3. Удалить пользователя системы\n4. Изменить права пользователя системы.\n')

# action = input('Введите соответствующую цифру ')
import user
import json
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
    if quest == '0':
        pass
    elif quest == '1':
        pass
    elif quest == '2':
        while answer == 'д':
            add_user()
            answer = input('Ввести еще одного пользователя? (д/н): ')
    elif quest == '3':
        pass
    elif quest == '4':
        pass
    elif quest == '0':
        pass 


def add_user():

    users_list = j_i_lst.json_in_lst('users.json')
    person = user.create_user()
    user.add_user_in_list(person, users_list)
    in_json.add_in_json(users_list, 'users.json')


# ****************преобразовать json в список

def delete_user():
    users_list = user.json_in_lst('users.json')


    



