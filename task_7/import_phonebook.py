import json
import logger
import sort_data


def import_ph_b():
    path = input('укажите абсолютный путь к файлу json для импорта: ')

    with open(path, 'r') as read_import:
        data = json.load(read_import)
    
    with open('phonebook.json', 'r') as read_phonebook:
        phonebook = json.load(read_phonebook)

    
    for i in range(len(data)):
        phonebook.append(data[i])
    
    phonebook = sort_data.sort_data(phonebook, 0)
    
    
    with open('phonebook.json', 'w') as write_file:
        json.dump(phonebook, write_file, ensure_ascii=False)

    
    logger.import_logger(path)

    return 

# import_ph_b()


