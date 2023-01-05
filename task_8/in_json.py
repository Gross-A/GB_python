
# добавление пользователей в результирующий файл json

import json


def add_in_json(item, file):
    with open(file, 'w') as data:
        json.dump(item, data, ensure_ascii=False)