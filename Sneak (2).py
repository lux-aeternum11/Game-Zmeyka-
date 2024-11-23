import pygame
from random import randrange
from random import randint


RES = 800
SIZE = 100
koef = SIZE/50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
rat = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
portal = randrange(0, RES, SIZE), randrange(0, RES, SIZE)



ruins = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
ruins1 = (ruins[0] + 50*koef, ruins[1])
ruins2 = (ruins[0] + 100*koef, ruins[1])
ruins3 = (ruins[0], ruins[1]+50*koef)
ruins4 = (ruins[0], ruins[1]+100*koef)

while apple == ruins or apple == ruins1 or apple == ruins2 or apple == ruins3 or apple == ruins4:
    apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

while rat == ruins or rat == ruins1 or rat == ruins2 or rat == ruins3 or rat == ruins4:
    rat = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

while portal == ruins or portal == ruins1 or portal == ruins2 or portal == ruins3 or portal == ruins4:
    portal = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

dris = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
snake = [(x, y)]

dx, dy = 0, 0
fps = 20 #скорость
frame_speed = 5
frame_counter = 0

ran_num_rat = [0]
ran_num_ruins = [0]

points = 0
# show_points = pygame.font.SysFont('arial', 26, bold=True)
# score = show_points.render(f'ОЧКИ: {points}', 1,pygame.Color('green'))

rat_eaten = 0
portal_eaten = 0
spawned_ruins = 0

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
# sc.blit(score, (5, 5))

while True:
    frame_counter += 1
    sc.fill(pygame.Color('black'))


    [(pygame.draw.rect(sc, pygame.Color('white'), (i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))

    ruins1 = (ruins[0] + 50 * koef, ruins[1])
    ruins2 = (ruins[0] + 100 * koef, ruins[1])
    ruins3 = (ruins[0], ruins[1] + 50 * koef)
    ruins4 = (ruins[0], ruins[1] + 100 * koef)

     # движения змеи
    if frame_counter % frame_speed == 0:
       x += dx * SIZE
       y += dy * SIZE
       snake.append((x, y))
       snake = snake[-length:]
    # поедание
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        fps += 3
        random_num = randint(0, 101)
        ran_num_rat.append(random_num)
        ran_num_ruins.append(random_num)
        rat_eaten = 0
        points += 1
    print(ran_num_rat)

    if ran_num_ruins[-1]>= 20:
        pygame.draw.rect(sc, pygame.Color('#3b1306'), (*ruins, SIZE + 2 * SIZE, SIZE))
        pygame.draw.rect(sc, pygame.Color('#3b1306'), (*ruins, SIZE, SIZE + 2 * SIZE))


        if snake[-1] == ruins or snake[-1] == ruins1 or snake[-1] == ruins2 or snake[-1] == ruins3 or snake[-1] == ruins4:
            print('Вы умерли!')
            print(f'Ваши очки: {points}')

            break



    if ran_num_rat[-1] >= 30 and rat_eaten == 0:
        pygame.draw.rect(sc, pygame.Color('#33302f'), (*rat, SIZE, SIZE))
        if snake[-1] == rat:
            rat = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
            length += 3
            fps -= 10
            rat_eaten = 1
            points += 1

    if points >= 5 and portal_eaten == 0:
        pygame.draw.rect(sc, pygame.Color('#7d0a8a'), (*portal, SIZE, SIZE))
        if snake[-1] == portal:
            portal = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
            fps += 10
            portal_eaten = 1
            SIZE = 50
            koef = SIZE/50




       # конец игры
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE:
        print('Вы умерли!')
        print(f'Ваши очки: {points}')

        break
    if len(snake) != len(set(snake)):
        print('Вы умерли!')
        print(f'Ваши очки: {points}')

        break


    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # управление
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dris['W']:
        dris = {'W': True, 'S': False, 'A': True, 'D': True}
        dx, dy = 0, -1
    if key[pygame.K_s] and dris['S']:
        dx, dy = 0, 1
        dris = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dris['A']:
        dx, dy = -1, 0
        dris = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dris['D']:
        dx, dy = 1, 0
        dris = {'W': True, 'S': True, 'A': False, 'D': True}

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
