'''запись результирующего списка справочника в файл json для дальнешей работы с ним (разобраться - почему записывает кодировку символов строки а не саму строку)'''

import json
import input_data as inp_d

phonebook = inp_d.input_person()

with open('phonebook.json', 'w') as write_phonebook:
    json.dump(phonebook, write_phonebook)
