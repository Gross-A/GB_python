from datetime import datetime as dt
from time import time

def add_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{} - добавлены записи в кол-ве {} шт. \n'
                    .format(time,data))


def export_logger(data):
    time = dt.now().strftime('%d/%m/%y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{} - справочник выгружен во внешний файл:{}\n'
                    .format(time,data))


def import_logger(data):
    time = dt.now().strftime('%d/%m/%y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{} - справочник импортирован из: {}\n'
                    .format(time,data))


def terminal_logger():
    time = dt.now().strftime('%d/%m/%y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{} - вывод справочника в консоль\n'
                    .format(time))
