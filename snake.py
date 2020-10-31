import pygame
import random
import pygame.mixer
pygame.init()
#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

pygame.mixer.init()

#specific variables
txt = pygame.font.SysFont(None, 55)
def print_text(text,color,x,y):
    screen_txt=txt.render(text,True,color)
    gamewind.blit(screen_txt,[x,y])
food_x = random.randint(0, 900)
food_y = random.randint(0, 600)
snake_list=[]
snake_length=1

def plot_snake(gamewind,white,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewind, white, [x, y, snake_size, snake_size])

clock=pygame.time.Clock()
 #creating screen
gamewind=pygame.display.set_mode((900,600))
pygame.display.set_caption("sankegame")
gamewind.fill(red)
pygame.display.update()

bgimg = pygame.image.load("bgim.jpg")
bgimg = pygame.transform.scale(bgimg, (900, 600)).convert_alpha()
#welcome
def welcome():
    exit=False
    while not exit:
        pygame.mixer.music.load("Forget Me Not - Patrick Patrikios.mp3")
        pygame.mixer.music.play()
        gamewind.blit(bgimg, (0, 0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_loop()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()

#game_over = False
def game_loop():
    exit_game = False
    snake_x = 55
    snake_y = 45
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    fps = 30
    food_size = 10
    score = 0
    game_over = False
    with open("highscore.txt", "r") as f:
        hiscore = f.read()
    food_x = random.randint(0, 900)
    food_y = random.randint(0, 600)
    snake_list = []
    snake_length = 1
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(hiscore))
            gamewind.fill(white)
            print_text("your game is over ", black,255,275)
            print_text("Press Enter to continue", black,225,315)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    welcome()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x = 8
                        velocity_y = 0

                    if event.key==pygame.K_LEFT:
                        velocity_x = -8
                        velocity_y = 0
                    if event.key==pygame.K_UP:
                        velocity_y = -8
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 8
                        velocity_x = 0

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                food_x = random.randint(0, 900)
                food_y = random.randint(0, 600)
                score=score+10
                snake_length=snake_length+5
                if score>int(hiscore):
                    hiscore=score

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over=True
            gamewind.fill(red)
            print_text("Score: "+str(score)+"  Highscore: "+str(hiscore),black,5,5)
            plot_snake(gamewind,white,snake_list,snake_size)
            pygame.draw.rect(gamewind,black,[food_x,food_y,food_size,food_size])
            if snake_x<0 or snake_x>900 or snake_y<0 or snake_y>600:
                game_over=True
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()



