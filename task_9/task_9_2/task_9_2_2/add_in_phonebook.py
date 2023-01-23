'''модуль для добавления записей в уже существующий справочник'''
import json
from operator import itemgetter, attrgetter
import sort_data
import logger

# with open('phonebook.json', 'r') as read_file:
#     new_data = json.load(read_file)
def add_in_phonebook():

    with open('phonebook.json', 'r') as data_file:  #откроем существующий справочник
        phonebook = json.load(data_file)

    # print(phonebook)
    import input_data

    new_persons = input_data.input_person() #запрос ввода информации о новом абоненте
    count = 0   #количество добавленных пользователей
    for i in range(len(new_persons)):   #применим к каждому вновь введенному абоненту
        phonebook.append(new_persons[i]) 
        count += 1   #добавляем каждого нового абонента в результирующий списко абоненто
        phonebook_new = sort_data.sort_data(phonebook, 0) #сортируем список по фамилии в алф порядке
        with open('phonebook.json', 'w') as result_file:    #переписываем файл json с результирующим списком
            json.dump(phonebook_new, result_file, ensure_ascii=False)
    
    logger.add_logger(count)
    return phonebook_new

# add_in_phonebook()

