# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Тот, кто берет последнюю конфету - проиграл.
# игра с другом

import random
players = ['Первый игрок','Второй игрок']
sweets =221
max_step= 28
def game (sweets, max_step, players):
    count = 0
    first = random.randint(0, 1)
    print (f'Начинает игрок № {first + 1} ')
       
    while sweets > 0:
        step = int(input(f'{players[first % 2]} заберите конфеты (от 1 до 28):'))
        if step > max_step:
            print(f'Можно взять не более {max_step}')
            continue
        if step > sweets:
            print(f'Можно взять не более {sweets} ')
            continue
        sweets = sweets - step
        if sweets > 0:
            print(f'Осталось {sweets} конфет')
        else:
            print('Игра окончена')
        first += 1
        count += 1
    return players[first % 2]
 
winer = game (sweets, max_step, players)
print(f'Победил {winer}')