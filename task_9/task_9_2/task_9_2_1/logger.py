
import work_with_json as w_json
from pathlib import Path




# def write_in_file(data, filename):
#     with open(filename, 'a') as data_file:  #откроем существующий файл
#         data = json.load(data_file)
#     return data


def check_data(veriied_data, prototype):
    if veriied_data == prototype:
        return True
    else:
        return False


def check_login():
    nickname = input('введите никнэйм: ')
    account_data = w_json.json_in_lst('account_data.json')
    for i in account_data:

        if check_data(nickname, i['nickname']):
            passw = input('введите пароль: ')
            if check_data(passw, i['password']):
                return True
            else:
                print('введен неверный никнэйм или пароль. Попробуйте снова.')
                check_login()
        

def register():
    nickname = input('введите никнэйм: ')
    path = Path('account_data.json')
    lst = w_json.json_in_lst(path)
    # print(lst)

    if len(lst) == 0:
        password = input('введите пароль не менее 4 знаков: ')
        person_data = dict(nickname = nickname, password = password)
        lst.append(person_data)

        w_json.add_in_json(lst, path)
    
    elif len(lst) > 0:
        check = True

        for i in range(len(lst)-1):
            # print(lst[i]['nickname'])
            if nickname == lst[i]['nickname']:
                check = False
                break

        # print(lst[i]['nickname'])
        # print(check)

        if check == True:
            password = input('введите пароль не менее 4 знаков: ')

            person_data = dict(nickname = nickname, password = password)
            

            lst.append(person_data)

            w_json.add_in_json(lst, path)
        elif check == False:
            print('такой никнэйм уже существует')
            register()


# register()





