# преобразование данных из файла json в список

import json


def json_in_lst(file):
    with open(file, 'r') as read_json:
        return json.load(read_json)
