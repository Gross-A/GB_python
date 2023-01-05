import json
import set_task


class User():
    user_count = 0
    # конструктор
    def __init__(self, name, department, job_title, log, passw):
        # self.name = ''
        # self.department = ''
        # self.job_title = ''
        # self.log = ''
        # self.passw = ''
        # User.user_count += 1
        # ********************
        self.name = name
        self.department = department
        self.job_title = job_title
        self.log = log
        self.passw = passw
        User.user_count += 1


# сюда же нужно функции постановки задачи, отчета о выполненной задаче
# просмотр задач и т.д.
    def show_user_info(self):
        print(self.name)
        print(f'Подразделение: {self.department}')
        print(f'Должность: {self.job_title}')
        print(f'Логин: {self.log}')



    def input_login(self):
        return input('Введите логин: ')


    def input_passw(self):
        return input('введите пароль: ')


    def input_user_type(self):
        user_type = input('Введите статус пользователя.\n1 - начальник подразделения,\n2 - сотрудник')
        return user_type
    

def create_user():
       
    name = input('введите имя пользователя: ')
    user_status = input('введите статус пользователя: 0 - администратор/1 - руководитель/2 - исполнитель: ')
    department = input('введите название подразделения: ')
    job_title = input('введите должность: ')
    log = input('введите логин пользователя: ')
    passw = input('введите пароль: ')

    ask = input('Создать пользователя? (д/н): ')
    
    if ask == 'д':
        user = dict(name = name, 
                    user_status = user_status,
                    department = department, 
                    job_title = job_title,
                    log = log,
                    passw = passw)
        return user

    elif ask == 'н':
        pass # здесь должен быть вызов функции вызова стартового экрана


def add_user_in_list(item, lst):
    lst.append(item)



def show_manager_menu(department):
    # print('manager')
    quest = input('Выберите действие:\n1 - вывести список сотрудников\n2 - поставить задачу подчиненному\n0 - выйти.\nВаш выбор: ')
    if quest == '0':
        pass
    elif quest == '1':
        set_task.show_staff(department)
        question = input('выполнить другое действие? (д/н): ')

        if question == 'д':
            show_manager_menu(department)
        else:
            pass
    elif quest == '2':
        set_task.set_task(department)
        question = input('выполнить другое действие? (д/н): ')

        if question == 'д':
            show_manager_menu(department)
        else:
            pass

    elif quest == '0':
        pass 



def show_employee_menu(user_name):
    quest = input('Выберите действие:\n1 - посмотреть активные задания\n2 - написать сообщение пользователю\n0 - выйти.\nВаш выбор: ')

    if quest == '0':
        pass
    elif quest == '1':
        set_task.show_tasks(user_name)
    elif quest == '2':
        # write_message()
        pass
    elif quest == '0':
        pass 



    

