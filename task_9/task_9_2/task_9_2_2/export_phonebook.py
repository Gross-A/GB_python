import json
import logger


def present_data():

    with open('phonebook.json', 'r') as read_file:
        data = json.load(read_file)

    # print(data)

    sep_1 = ''
    # sep_2 = ''
    sep_2 = '\n------------------------------------------------------------\n'


    format = input('пожалуйста укажите в каком формате выводить данные 1 - горизонтальном, 2 - вертикальном: ')
    ext = input('введите название файла (с расширением) для выгрузки справочника:  ')

    if format == '1':
        sep_1 = '   '
        # sep_2 = '\n------------------------------------------------------------'
    elif format == '2':
        sep_1 = '\n'

    for i in range(len(data) - 1):
        person_out_line = f'Фамилия: {data[i][0]}{sep_1}Имя: {data[i][1]}{sep_1}Телефон: {data[i][2]}{sep_1}Доп информация: {data[i][3]}{sep_2}  '

        with open(ext, 'a') as file:
            file.write(person_out_line)
    
    logger.export_logger(ext)

# present_data()