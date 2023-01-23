import json


def json_in_lst(file):
    with open(file, 'r') as read_json:
        return json.load(read_json)


# def open_json(filename):

#     with open(filename, 'r') as data_file:  #откроем существующий файл
#         data = json.load(data_file)
#     return data


def add_in_json(item, file):
    with open(file, 'w') as data:
        json.dump(item, data, ensure_ascii=False)

