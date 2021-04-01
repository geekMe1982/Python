import pygame
import random
import time

pygame.init()




red = (255, 0, 0)
pink = (190, 150, 170)
white = (255, 255, 255)

window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Snake game by SVETA')

snake_block = 10
snake_speed = 30

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 30)

#Вывод текст на экран
def message(msg, color2):
    text = font_style.render(msg, True, color2)
    window.blit(text, [window_width/3, window_height/3])


def game_loop():
    game_over = False
    game_close = False

    x1 = window_width/2
    y1 = window_height/2

    x1_change = 0
    y1_change = 0

    x_food = round(random.randrange(0, window_width - snake_block) / 10.0)
    y_food = round(random.randrange(0, window_width - snake_block) / 10.0)

    while not game_over:

        while game_close == True:
            window.fill(white)
            message('you lost, press Q to quit or c to continue', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key  == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                #Нажатие кнопки вниз
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
                #Если нажать на кнопку spa
                elif event.key == pygame.K_SPACE:
                    x1_change = 0
                    y1_change = 0


        if x1>= window_width or x1 < 0 or y1>=window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(pink)

        pygame.draw.rect(window, 'green', [x_food, y_food, snake_block, snake_block])
        pygame.draw.rect(window, snake_color(), [x1, y1, snake_block , snake_block])
        pygame.draw.circle(window, snake_color(), [x1, y1 + 5], 5)
        pygame.display.update()

        clock.tick(snake_speed)



    pygame.quit()
    quit()
game_loop()
