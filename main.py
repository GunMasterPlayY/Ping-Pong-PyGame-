import pygame , sys , random

pygame.init()

WIDTH, HEIGHT = 1000,700
BACKGROUND = (0,0,0)
PLAYER_COLOR = (255,255,255)
UNIT_SIZE = 20
PLAYER_WIDTH = UNIT_SIZE
PLAYER_HEIGHT = UNIT_SIZE*5

clock = pygame.time.Clock()
left_player = None
right_player = None
ball = None
l_pos = 200
r_pos = 200
ball_x,ball_y = 0,0
direction = "SE"
r_score  = 0
l_score = 0


window = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font("freesansbold.ttf",25)

def ball_move():
    global ball_x,ball_y
    if direction == "SE":
        ball_x+=2.5*2
        ball_y+=2.5*2
    elif direction == "SW":
        ball_x-=2.5*2
        ball_y+=2.5*2
    elif direction == "NW":
        ball_x-=2.5*2
        ball_y-=2.5*2
    elif direction == "NE":
        ball_x+=2.5*2
        ball_y-=2.5*2

def draw():
    global left_player,right_player,ball
    window.fill(BACKGROUND)

    left_player = pygame.Rect(0,l_pos,PLAYER_WIDTH,PLAYER_HEIGHT)
    pygame.draw.rect(window,PLAYER_COLOR,left_player)

    right_player = pygame.Rect(WIDTH-UNIT_SIZE,r_pos,PLAYER_WIDTH,PLAYER_HEIGHT)
    pygame.draw.rect(window,PLAYER_COLOR,right_player)

    ball = pygame.Rect(ball_x,ball_y,UNIT_SIZE,UNIT_SIZE)
    pygame.draw.rect(window,PLAYER_COLOR,ball)


    p1_score = font.render("Player 1 score: " + str(l_score) ,True,PLAYER_COLOR,(0,0,0))
    p2_score = font.render("Player 2 score: " + str(r_score),True,PLAYER_COLOR,(0,0,0))
    
    window.blit(p2_score,(WIDTH-210,10))
    window.blit(p1_score,(10,10))

    ball_move()

    pygame.display.update()


def keyHandler(key):
    global l_pos,r_pos
    if key[pygame.K_w] and l_pos>=0:
        l_pos-=2.5*2
    elif key[pygame.K_s]  and l_pos <= HEIGHT - PLAYER_HEIGHT:
        l_pos+=2.5*2
    elif key[pygame.K_UP] and r_pos>=0:
        r_pos-=2.5*2
    elif key[pygame.K_DOWN] and r_pos<=HEIGHT -PLAYER_HEIGHT:
        r_pos+=2.5*2

def countdown():
    font = pygame.font.Font("freesansbold.ttf",200)
    for i in range(1,4):
        number = font.render(str(i),True,PLAYER_COLOR,(0,0,0))
        window.blit(number,(450,225))
        pygame.display.update()
        clock.tick(2)



def new_ball():
    global ball_x, ball_y

    countdown()


    while True:
        ball_x = random.randint(350,450)
        if ball_x% UNIT_SIZE == 0:
            break

    while True:
        ball_y = random.randint(250,450)
        if ball_y% UNIT_SIZE == 0:
            break

def direction_changer():
    global direction
    if ball_y <= 0:
        if direction == "NW":
            direction = "SW"
        elif direction == "NE":
            direction = "SE"
    elif ball_y+UNIT_SIZE >= HEIGHT:
        if direction == "SW":
            direction = "NW"
        elif direction == "SE":
            direction = "NE"
    if ball.colliderect(left_player):
        if direction == "SW":
            direction = "SE"
        elif direction == "NW":
            direction = "NE"
    elif ball.colliderect(right_player):
        if direction == "SE":
            direction = "SW"
        elif direction == "NE":
            direction = "NW"


def score_adder():
    global l_score,r_score,ball_x,ball_y
    if ball_x<=0:
        r_score +=1
    elif ball_x+UNIT_SIZE>=HEIGHT:
        l_score +=1


def check_collision():
    if ball_x <= 0:
        score_adder()
        new_ball()
    elif ball_x+UNIT_SIZE >= WIDTH:
        score_adder()
        new_ball()


if __name__ == '__main__':
    new_ball()
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keyHandler(pygame.key.get_pressed())
        draw()
        direction_changer()
        check_collision()
        clock.tick(60)
