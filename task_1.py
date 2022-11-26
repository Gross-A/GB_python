# task1


# def vocation():
#     day = int(input('введите день недели от 1 до 7: '))
#     if day == 6:
#         print('да')
#     elif day == 7:
#         print('да')
#     else:
#         print('нет')


# vocation()


# task2

# task2

x = [True, False]
y = [True, False]
z = [True, False]

count = 0
countR = 0
for i in x:
    for j in y:
        for u in z:
            count += 1
            if (not (x[i] or y[j] or z[u])) != (not x[i] and not y[j] and not z[u]):
                print('утверждение не верно в случае X = {x[i]}, Y = {y[j]}, Z = {z[u]}')
            else:
                countR += 1
if(countR == count):
    print('утверждение верно при любых X, Y, Z')



# task3

# def define_range():
#     variant = {
#         1: 'x > 0, y > 0',
#         2: 'x < 0, y > 0',
#         3: 'x < 0, y < 0',
#         4: 'x > 0, y < 0',
#     }
#     x = int(input('введите интересующую четверть: '))
#     print('точка на оси: ', variant[x])


# define_range()


# task4 округляет до второго знака после запятой по арифметическим правилам


# def calc_distance():
#     pointA = input('input coordinate of pointA x,y:  ').split(',')
#     pointB = input('input coordinate of pointB x,y:  ').split(',')

#     s = round((abs(int(pointA[0]) - int(pointB[0]))**2 + abs(int(pointA[1]) - int(pointB[1]))**2)**0.5, 2)

#     print('length:  ', s)


# calc_distance()
