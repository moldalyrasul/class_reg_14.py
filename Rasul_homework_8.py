import random
import datetime

name = input('Введите имя: ')
bat = int(input('Количество попыток: '))
bet = bat
start = datetime.datetime.now()
with open('results.txt', 'w', encoding='UTF-8') as file:
    while bat != 0:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        v = a*b
        try:
            answer = int(input(f'{a} * {b} = ?'))
            bat -= 1
            if answer == v:
                print(f'Правильно Ответ: {v}')
                print(f'Осталось: {bat} попыток')
                file.write(f'{a} * {b} ={answer} ({v})- правильно\n')
            else:
                print(f'Неправильно Ответ: {v}')
                print(f'Осталось: {bat} попыток')
                file.write(f'{a} * {b} ={answer} ({v})- неправильно\n')
        except ValueError:
            print('Вводить только целые числа')

    time = datetime.datetime.now() - start
    print(time)
    file.write(f'было {bat} попыток, потрачено времени {time}, имя: {name}\n')




