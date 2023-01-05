'''выбрать работника подразделения (файл json  в список, перебрать весь список, 
если значение ключа department совпадает с значением руководителя, то добавить в список 
работников отдела department_staff_list )
написать задание, указать срок исполнения
добавить в файл "tasks.json"'''

import json_in_list
import in_json

# создание листа с сотрудниками отдельного подразделения компании


def make_staff_list(department):
    department_staff_list = []
    staff_list = json_in_list.json_in_lst('users.json')
    staff_id = 0
    for i in staff_list:
        if i['department'] == department:
            staff_id += 1
            person = [staff_id, i['name'], i['job_title']]
            department_staff_list.append(person)
    
    return department_staff_list

#  вывод в консоль списка сотрудников выбранного подразделения



def show_staff(department):
    lst = make_staff_list(department)
    print('Список сотрудников: \n')

    for i in lst:
        print(f'№: {i[0]}, имя: {i[1]}, должность: {i[2]}')
    
    return len(lst)

tasks_list = []


def set_task(department):
    question = input('Вывести список сотрудников подразделения для выбора? (д/н): ')

    if question == 'д':
        number = show_staff(department)
        choice = int(input('введите номер сотрудника из списка: ')) - 1
        task = input('введите поручение: ')
        time = input('введите контрольный срок исполнения: ')
        staff_list = make_staff_list(department)
        # print(staff_list)

        name = staff_list[choice][1]

        tasks_list = json_in_list.json_in_lst('tasks.json')

        person = dict(name = name, task = task, time = time, status = 'inactive')
        
        tasks_list.append(person)

        in_json.add_in_json(tasks_list, 'tasks.json')



def show_tasks(person):
    lst = json_in_list.json_in_lst('tasks.json')
    
    for i in lst:
        if i['name'] == person and i['status'] == 'inactive':
            task = i['task']
            time = i['time']
            print(f'задание: {task}, срок: {time}')




        
  


