import time
import datetime
from random import randint, sample

cash = 500

while cash != 0:
    bet = int(input(
        'Введите ставку!'
        f'Доступно: {cash}\n'
    ))
    comp = [randint(1, 6), randint(1, 6)]
    user = [randint(1, 6), randint(1, 6)]
    if sum(comp) > sum(user):
        cash -= bet
        with open('results.txt', 'a') as file:
            file.write(f'comp: {comp} - user: {user}'
                       f" Вы проиграли! {sum(comp)} > {sum(user)}\n"
                       )
    elif sum(comp) < sum(user):
        cash += bet
        with open('results.txt', 'a') as file:
            file.write(f'comp: {comp} - user: {user}'
                       f" Вы выиграли! {sum(comp)} < {sum(user)}\n"
                       )
    else:
        with open('results.txt', 'a') as file:
            file.write(f'comp: {comp} - user: {user}'
                       f" Ничья! {sum(comp)} = {sum(user)}\n"
                       )

    with open('results.txt', 'r') as file:
        print(file.read())


# print(sample(range(1, 6), 2))
# print(randint(1, 6), randint(1, 6))








# with open('new_file.txt', 'r', encoding='UTF-8') as file:
#     for i in file.readlines():
#         print(i, end='')
#         time.sleep(1)

# with open('text.txt', 'w') as file:
#     file.write('Python 3.9')
#
# with open('new_text.txt', 'a') as file:
#     file.write('\n Best programing language!')


