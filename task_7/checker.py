import re

'''проверка на правильность заполнения полей формы ввода or inp_data[2] != r'8\d{10}'''
# inp_data = ('абак', 'Кузя', '+79559631258', 'sdf')


def check_correct(inp_data):
    correct = True

    if not re.search(r'[А-Яа-я]',inp_data[0]):
        print('Некорректно введена фамилия')
        correct = False
    elif not re.search(r'[А-Яа-я]',inp_data[1]):
        print('Некорректно введено имя')
        correct = False
    elif not re.search(r'8\d{10}|[+]7\d{10}',inp_data[2]):
        print('Некорректно введено номер телефона')
        correct = False
    
    return correct

# res = check_correct(inp_data)

# print(res)



