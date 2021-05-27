import pygame
import sys
import random
from TextInput import InputBox
from Requests import Requests

errors = pygame.init()  # Errors
display = pygame.display.set_mode((960, 540))  # Window size
pygame.display.set_caption('Snake Game')  # Window title
fps = pygame.time.Clock()  # FPS
position = [100, 50]  # Start position
snake = [[100, 50], [90, 50], [80, 50]]  # snake size
#  generating food
food = [random.randrange(1, 95) * 10, random.randrange(1, 53) * 10]
spawn = True
pointer, direction = 'DOWN', 'DOWN'  # The initial movement of the snake
score = 0  # Start score


#  'Game over' window
def GameOver():
    clock = pygame.time.Clock()
    text_input = InputBox(380, 185, 140, 32)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user clicks on the cross, the game is closed
                pygame.quit()  # Closing the game
                sys.exit()  # Closing the program
            player = text_input.handle_event(event)

            if player == None:
                pass
            else:
                Requests.Post(player, score)

        text_input.update()

        display.fill((234, 239, 244))

        #  The text 'Game Over!'
        gameover_text = pygame.font.SysFont('arial', 72).render('Game Over!', True,
                                                                pygame.Color(230, 0, 0))  # Font color, size and family
        gameover_text_position = gameover_text.get_rect()
        gameover_text_position.midtop = (480, 25)  # Text position
        display.blit(gameover_text, gameover_text_position)

        #  The text 'Best players'
        enter_your_nickname = pygame.font.SysFont('monaco', 26).render('Best players:', True, pygame.Color(0, 0,
                                                                                                           0))  # Font color, size and family
        enter_your_nickname_position = enter_your_nickname.get_rect()
        enter_your_nickname_position.midtop = (480, 240)
        display.blit(enter_your_nickname, enter_your_nickname_position)

        #  Table title
        enter_your_nickname = pygame.font.SysFont('monaco', 26).render('#                 Player                Score',
                                                                       True, pygame.Color(0, 0,
                                                                                          0))  # Font color, size and family
        enter_your_nickname_position = enter_your_nickname.get_rect()
        enter_your_nickname_position.midtop = (495, 268)
        display.blit(enter_your_nickname, enter_your_nickname_position)

        #  Best players
        height, n = 300, 1
        for i in Requests.Get():
            lst = [str(n), str(Requests.Get()[str(n)]['player']),
                   str(Requests.Get()[str(n)]['score'])]
            records_text = pygame.font.SysFont('monaco', 26).render(
                str("{: >20} {: >20} {: >20}".format(
                    lst[0], lst[1], lst[2])), True,
                pygame.Color(0, 0, 0))  # Font color, size and family
            records_text_position = gameover_text.get_rect()
            records_text_position.midtop = (465, height)  # Text position
            display.blit(records_text, records_text_position)
            height += 27
            n += 1

        #  The text 'Enter your nickname'
        enter_your_nickname = pygame.font.SysFont('monaco', 26).render('Enter your nickname:', True, pygame.Color(0, 0,
                                                                                                                  0))  # Font color, size and family
        enter_your_nickname_position = enter_your_nickname.get_rect()
        enter_your_nickname_position.midtop = (480, 160)
        display.blit(enter_your_nickname, enter_your_nickname_position)

        #  Text input
        text_input.draw(display)

        #  View score
        Score(1)


#  View score
def Score(choice=0):
    text = pygame.font.SysFont('monaco', 26).render('Score: {0}'.format(score), True,
                                                    pygame.Color(0, 0, 0))  # Font color, size and family
    text_position = text.get_rect()
    if choice == 0:
        text_position.midtop = (40, 10)  # Text position
    else:
        text_position.midtop = (480, 125)  # Text position after 'Game over'
    display.blit(text, text_position)
    pygame.display.flip()


#  Game logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user clicks on the cross, the game is closed
            pygame.quit()  # Closing the game
            sys.exit()  # Closing the program

        #  Click tracking
        elif event.type == pygame.KEYDOWN:  # If the user clicks on the buttons
            if event.key == event.key == ord('d'):
                pointer = 'RIGHT'  # If the user presses the 'd' button, the snake moves to the right
            elif event.key == event.key == ord('a'):
                pointer = 'LEFT'  # If the user presses the 'a' button, the snake moves to the left
            elif event.key == event.key == ord('w'):
                pointer = 'UP'  # If the user presses the 'w' button, the snake moves up
            elif event.key == event.key == ord('s'):
                pointer = 'DOWN'  # If the user presses the 's' button, the snake moves down

    #  Snake movement
    if pointer == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'  # To the right
    elif pointer == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'  # To the left
    elif pointer == 'UP' and not direction == 'DOWN':
        direction = 'UP'  # Up
    elif pointer == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'  # Down

    #  Changing the position of the snake
    if direction == 'RIGHT':
        position[0] += 10  # To the right
    elif direction == 'LEFT':
        position[0] -= 10  # To the left
    elif direction == 'UP':
        position[1] -= 10  # Up
    elif direction == 'DOWN':
        position[1] += 10  # Down

    #  Snake body
    snake.insert(0, list(position))
    if position[0] == food[0] and position[1] == food[1]:  # If the snake ate the food
        score += 1
        spawn = False
    else:
        snake.pop()

    #  Generating food
    if spawn == False:
        #  Generating food
        food = [random.randrange(1, 95) * 10, random.randrange(1, 53) * 10]
    spawn = True

    #  Background color
    display.fill(pygame.Color(234, 239, 244))

    #  Snake color
    for pos in snake:
        pygame.draw.rect(display, pygame.Color(0, 225, 0),
                         pygame.Rect(pos[0], pos[1], 10, 10))

    #  Food color
    pygame.draw.rect(display, pygame.Color(230, 0, 0),
                     pygame.Rect(food[0], food[1], 10, 10))

    #  The limits of Snake Death
    if position[0] > 959 or position[0] < 0:  # By width
        GameOver()  # Transfer to the "Game Over" page"
    if position[1] > 539 or position[1] < 0:  # По высоте
        GameOver()  # Transfer to the "Game Over" page"

    #  Если змейка врежится сама в себя
    for i in snake[1:]:
        if position[0] == i[0] and position[1] == i[1]:
            GameOver()  # Transfer to the "Game Over" page"

    Score()
    fps.tick(12)  # FPS
