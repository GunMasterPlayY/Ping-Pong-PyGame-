import pygame , sys , random

pygame.init()

WIDTH, HEIGHT = 800,700
BACKGROUND = (0,0,0)
PLAYER_COLOR = (255,255,255)
UNIT_SIZE = 25
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


window = pygame.display.set_mode((WIDTH, HEIGHT))

def ball_move():
    global ball_x,ball_y
    if direction == "SE":
        ball_x+=2.5
        ball_y+=2.5
    elif direction == "SW":
        ball_x-=2.5
        ball_y+=2.5
    elif direction == "NW":
        ball_x-=2.5
        ball_y-=2.5
    elif direction == "NE":
        ball_x+=2.5
        ball_y-=2.5

def draw():
    global left_player,right_player,ball
    window.fill(BACKGROUND)

    left_player = pygame.Rect(0,l_pos,PLAYER_WIDTH,PLAYER_HEIGHT)
    pygame.draw.rect(window,PLAYER_COLOR,left_player)

    right_player = pygame.Rect(WIDTH-UNIT_SIZE,r_pos,PLAYER_WIDTH,PLAYER_HEIGHT)
    pygame.draw.rect(window,PLAYER_COLOR,right_player)

    ball = pygame.Rect(ball_x,ball_y,UNIT_SIZE,UNIT_SIZE)
    pygame.draw.rect(window,PLAYER_COLOR,ball)

    ball_move()

    pygame.display.update()


def keyHandler(key):
    global l_pos,r_pos
    if key[pygame.K_w] and l_pos>=0:
        l_pos-=2.5
    elif key[pygame.K_s]  and l_pos <= HEIGHT - PLAYER_HEIGHT:
        l_pos+=2.5
    elif key[pygame.K_UP] and r_pos>=0:
        r_pos-=2.5
    elif key[pygame.K_DOWN] and r_pos<=HEIGHT -PLAYER_HEIGHT:
        r_pos+=2.5

def score_adder():
    pass

def new_ball():
    while True:
        ball_x = random.randint(0,WIDTH)
        if ball_x% UNIT_SIZE == 0:
            break

    while True:
        ball_y = random.randint(0,HEIGHT)
        if ball_y% UNIT_SIZE == 0:
            break


def score_adder():
    pass


def check_collision():
    global ball_x, ball_y
    collided_ball = None
    if ball_y == l_pos and ball_x == 0:
        collided_ball = left_player
    elif ball_y == r_pos and ball_x == WIDTH-UNIT_SIZE:
        collided_ball = right_player
    new_ball()

if __name__ == '__main__':
    new_ball()
    print("HA")
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keyHandler(pygame.key.get_pressed())
        check_collision()
        draw()
        clock.tick(60)
