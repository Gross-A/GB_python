import json


def search_person():

    with open('phonebook.json', 'r') as read_file:
            data = json.load(read_file)

    search = input('Введите фамилию нужного абонента: ')

    count = 0
    for i in range(len(data)):
        if data[i][0] == search:
            output = f'\nФамилия: {data[i][0]}  Имя: {data[i][1]}  Телефон: {data[i][2]}'
            count += 1
            print(output)

    if count == 0:
        print('\nПоиск завершен. Такого абонента не найдено')


# search_person()