import random
import datetime

name = input('Введите имя: ')
attempt = int(input('Кол-во попыток: '))
attempt_d = attempt
start = datetime.datetime.now()
with open('results.txt', 'w', encoding='UTF-8') as file:
    while attempt != 0:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        v = a*b
        try:
            answer = int(input(f'{a} * {b} = ?'))
            attempt -= 1
            if answer == v:
                print(f'Правильно Ответ: {v}')
                print(f'Осталось: {attempt} попыток')
                file.write(f'{a} * {b} ={answer} ({v})- правильно\n')
            else:
                print(f'Неправильно Ответ: {v}')
                print(f'Осталось: {attempt} попыток')
                file.write(f'{a} * {b} ={answer} ({v})- неправильно\n')
        except ValueError:
            print('Вводить только целые числа')

    time = datetime.datetime.now() - start
    file.write(f'было {attempt_d} попыток, потрачено времени {time}, имя: {name}\n')




