import pygame
import random
import os
pygame.mixer.init()
pygame.init()
# Colors
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# Creating window
screen_width = 1050
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
#Background Image
bgimg = pygame.image.load("background1snak11.jpg")
intro = pygame.image.load("Design by Nikhil kumar123.png")
outro = pygame.image.load("gamov133.png",)
# Game Title
pygame.display.set_caption("Snakes With Nikhil")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont('bitstreamverasans', 50)
# Music
pygame.mixer.music.load('back.mp3.mp3')
pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(.6)



def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.blit(intro, (0,0))
        text_screen("start -> press space bar", white, 50, 490)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    # Check if hiscore file exists
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 40
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.blit(outro, (0, 0))
            text_screen("Game Over! Press Enter To Continue",white, 140, 500)
    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('back.mp3.mp3')
                        pygame.mixer.music.play(100)
                        pygame.mixer.music.set_volume(.6)
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                        pygame.mixer.music.load('tunetank.com_select-point.wav')
                        pygame.mixer.music.play()

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                        pygame.mixer.music.load('tunetank.com_select-point.wav')
                        pygame.mixer.music.play()
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                        pygame.mixer.music.load('tunetank.com_select-point.wav')
                        pygame.mixer.music.play()

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                        pygame.mixer.music.load('tunetank.com_select-point.wav')
                        pygame.mixer.music.play()

                    if event.key == pygame.K_q:
                        score +=10
                        pygame.mixer.music.load('tunetank.com_select-point.wav')
                        pygame.mixer.music.play()

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<12 and abs(snake_y - food_y)<12:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), black, 500, 6
                        
                        
                        )
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3.mp3')
                pygame.mixer.music.play(1)
                pygame.mixer.music.set_volume(.6)
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
