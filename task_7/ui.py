'''модуль для вывода приветствия, запроса на конкретное действие'''

# import input_data
import add_in_phonebook as add_pers
import export_phonebook
import import_phonebook
import search_person as search_p
import present_in_terminal as pres_term


def make_choice():
    hello = 'Что Вы хотите сделать?:\n1. Ввести информацию об абоненте. \n2. Вывести справочник в консоль. \n3. Найти абонента в справочнике \n4. Экспортировать справочник в файл. \n5. Импортировать данные из файла. \nВведите номер пункта и нажмите "ввод"'
    print(hello)
    choice = input('Ваш выбор?: ')

    if choice == '1':
        return add_pers.add_in_phonebook()
    elif choice == '2':
        return pres_term.present_in_terminal()
    elif choice == '3':
        return search_p.search_person()
    elif choice == '4':
        return export_phonebook.present_data()
    elif choice == '5':
        return import_phonebook.import_ph_b()
    else:
        print('некорректный ответ')




