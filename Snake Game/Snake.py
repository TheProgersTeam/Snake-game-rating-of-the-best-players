import pygame
import sys
import random
import time
from TextInput import InputBox
from Requests import Requests

errors = pygame.init()  # Ошибки
display = pygame.display.set_mode((960, 540))  # Размер окна
pygame.display.set_caption('Snake Game')  # Заголовок
fps = pygame.time.Clock()  # FPS 
position = [100, 50]  # Начальное положение змейки
snake = [[100, 50], [90, 50], [80, 50]]  # размер змейки 
food = [random.randrange(1, 95) * 10, random.randrange(1, 53) * 10]  # Генерация еды
spawn = True # Спавн еды
pointer, direction = 'DOWN', 'DOWN'  # Начальное движение змейки
score = 0  # Начальный счёт


# Окно окончания игры
def GameOver():
    
    clock = pygame.time.Clock()
    text_input = InputBox(380, 185, 140, 32)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Если пользователь нажимает на крестик, то игра закрывается 
                pygame.quit()  # Закрытие игры
                sys.exit()  # Закрытие программы
            player = text_input.handle_event(event)
            
            if player == None:
                pass
            else:
                Requests.Post(player, score)
                
        text_input.update()

        display.fill((234, 239, 244))
     
        # Текст 'Game Over!'
        gameover_text = pygame.font.SysFont('arial', 72).render('Game Over!', True, pygame.Color(230, 0, 0))  # Размер текста, шрифт и цвет
        gameover_text_position = gameover_text.get_rect()
        gameover_text_position.midtop = (480, 25)  # Позиция текста
        display.blit(gameover_text, gameover_text_position)

        # Текст 'Best players'
        enter_your_nickname = pygame.font.SysFont('monaco', 26).render('Best players:', True, pygame.Color(0, 0, 0))   # Размер текста, шрифт и цвет
        enter_your_nickname_position = enter_your_nickname.get_rect()
        enter_your_nickname_position.midtop = (480, 240)
        display.blit(enter_your_nickname, enter_your_nickname_position)
        
        # Заголовок таблицы 
        enter_your_nickname = pygame.font.SysFont('monaco', 26).render('#                Player                Score', True, pygame.Color(0, 0, 0))   # Размер текста, шрифт и цвет
        enter_your_nickname_position = enter_your_nickname.get_rect() 
        enter_your_nickname_position.midtop = (495, 268)
        display.blit(enter_your_nickname, enter_your_nickname_position)

        # Лучшие игроки 
        height, n = 300, 1
        import pandas as pd
        for i in Requests.Get():
            lst = [str(n), str(Requests.Get()[str(n)]['player']), str(Requests.Get()[str(n)]['score'])]
            records_text = pygame.font.SysFont('monaco', 26).render( str("{: >20} {: >20} {: >20}".format(lst[0], lst[1], lst[2])) , True, pygame.Color(0, 0, 0))   # Размер текста, шрифт и цвет
            records_text_position = gameover_text.get_rect()
            records_text_position.midtop = (465, height)  # Позиция текста
            display.blit(records_text, records_text_position)
            height += 27
            n += 1

        # Текст 'Enter your nickname'
        enter_your_nickname = pygame.font.SysFont('monaco', 26).render('Enter your nickname:', True, pygame.Color(0, 0, 0))   # Размер текста, шрифт и цвет
        enter_your_nickname_position = enter_your_nickname.get_rect()
        enter_your_nickname_position.midtop = (480, 160)
        display.blit(enter_your_nickname, enter_your_nickname_position)

        # Поле ввода
        text_input.draw(display)

        # Отображаем счет после окончания игры
        Score(1) 

        
        
    #time.sleep(2)  # Временная задержка после окончания игры
    #pygame.quit()  # Закрытие игры
    #sys.exit()  # Закрытие программы


# Отображение счёта
def Score(choice=0):
    text = pygame.font.SysFont('monaco', 26).render('Score: {0}'.format(score), True, pygame.Color(0, 0, 0))   # Размер текста, шрифт и цвет
    text_position = text.get_rect()
    if choice == 0:
        text_position.midtop = (40, 10)  # Позиция текста
    else:
        text_position.midtop = (480, 125)  # Позиция текста после окончания игры
    display.blit(text, text_position)
    pygame.display.flip()


# Логика игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если пользователь нажимает на крестик, то игра закрывается 
            pygame.quit()  # Закрытие игры
            sys.exit()  # Закрытие программы

        # Отслеживание нажатий
        elif event.type == pygame.KEYDOWN:  # Если пользователь нажимает на кнопки
            if event.key == event.key == ord('d'):
                pointer = 'RIGHT'  # Если пользователь нажимает на кнопку 'd', то змейка движется вправо
            elif event.key == event.key == ord('a'):
                pointer = 'LEFT'  # Если пользователь нажимает на кнопку 'a', то змейка движется влево
            elif event.key == event.key == ord('w'):
                pointer = 'UP'  # Если пользователь нажимает на кнопку 'w', то змейка движется вверх
            elif event.key == event.key == ord('s'):
                pointer = 'DOWN'  # Если пользователь нажимает на кнопку 's', то змейка движется вниз

    # Движение змейки
    if pointer == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'  # Вправо
    elif pointer == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'  # Влево
    elif pointer == 'UP' and not direction == 'DOWN':
        direction = 'UP'  # Вверх
    elif pointer == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'   # Вниз

    # Изменение положения змейки
    if direction == 'RIGHT':
        position[0] += 10  # Вправо
    elif direction == 'LEFT':
        position[0] -= 10  # Влево
    elif direction == 'UP':
        position[1] -= 10  # Вверх
    elif direction == 'DOWN':
        position[1] += 10  # Вниз

    # Тело змейки
    snake.insert(0, list(position))
    if position[0] == food[0] and position[1] == food[1]:  # Если змейка съела еду)
        score += 1
        spawn = False
    else:
        snake.pop()

    # Генерация еды
    if spawn == False:
        food = [random.randrange(1, 95) * 10, random.randrange(1, 53) * 10]  # Генерация еды
    spawn = True

    # Цвет фона
    display.fill(pygame.Color(234, 239, 244))

    # Цвет змейки
    for pos in snake:
        pygame.draw.rect(display, pygame.Color(0, 225, 0), pygame.Rect(pos[0], pos[1], 10, 10))

    # Цвет еды
    pygame.draw.rect(display, pygame.Color(230, 0, 0), pygame.Rect(food[0], food[1], 10, 10))

    # Границы смерти змейки 
    if position[0] > 959 or position[0] < 0: # По ширине
        GameOver() # Перенос на страницу "Игра закончена" 
    if position[1] > 539 or position[1] < 0: # По высоте
        GameOver() # Перенос на страницу "Игра закончена" 

    # Если змейка врежится сама в себя
    for i in snake[1:]:
        if position[0] == i[0] and position[1] == i[1]:
            GameOver() # Перенос на страницу "Игра закончена" 


    Score()
    fps.tick(12) # FPS - скорость змейки 
