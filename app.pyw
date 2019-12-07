import pygame

pygame.init()

# Screen
screen = pygame.display.set_mode((900,500))
pygame.display.set_caption('Pong Game')
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)

screen_w = screen.get_width()
screen_h = screen.get_height()
# Ball
ballSize = 18
ballX = screen_w/2 - ballSize/2
ballY = screen_h/2 - ballSize/2
ballSpeedX = -0.05
ballSpeedY = 0.05
# Player paddle
paddle_w = 13
paddle_h = 85
paddleX = 30
paddleY = screen_h/2 - paddle_h/2
paddle_color = (10, 251, 108)
# AI paddle
aiX = screen_w - 30 - paddle_w/2
aiY = screen_h/2 - paddle_h/2
ai_color = (255, 204, 0)
# Scores
score_value_player = 0
score_value_AI = 0
score_font = pygame.font.Font('font.ttf', 64)

def drawBall(x, y):
    pygame.draw.rect(screen, (241, 255, 227), (x, y, ballSize, ballSize))

def drawPaddle(x, y, color):
    pygame.draw.rect(screen, color, (x, y, paddle_w, paddle_h))

def draw_score():
    score_text1 = score_font.render(str(score_value_player), True, (255,255,255))
    score_text2 = score_font.render(str(score_value_AI), True, (255,255,255))
    screen.blit(score_text1, (225, 70))
    screen.blit(score_text2, (screen_w - 225, 70))


def speedUp():
    global ballSpeedX
    global ballSpeedY

    # predX
    if ballSpeedX > 0 and ballSpeedX < 3:
        ballSpeedX += 0.05
    elif ballSpeedX < 0 and ballSpeedX < -3:
       ballSpeedX -= 0.05

    # PredY
    if ballSpeedY > 0 and ballSpeedY < 3:
        ballSpeedY += 0.05
    elif ballSpeedY < 0 and ballSpeedY < -3:
        ballSpeedY -= 0.05

# Main loop
run = True
while run:
    screen.fill((15,15,15))
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEMOTION:
            paddleY = pos[1] - paddle_h/2
    # Player paddle
    if paddleY <= 0:
        paddleY = 0
    elif paddleY >= screen_h - paddle_h:
        paddleY = screen_h - paddle_h
    # Ball bouncing
    if ballY <= 0 or ballY >= screen_h - ballSize:
        ballSpeedY = -ballSpeedY

    if ballX <= 0:
        score_value_AI += 1

    if ballX >= screen_w - ballSize:
        score_value_player += 1

    if ballX <= 0 or ballX >= screen_w - ballSize:
        ballX = screen_w/2 - ballSize/2
        ballY = screen_h/2 - ballSize/2

    # Ball touch player
    if ballX <= paddleX + paddle_w and ballY <= paddleY + paddle_h and ballY >= paddleY:
        ballSpeedX = -ballSpeedX
        speedUp()
    # Ball touch AI
    if ballX >= aiX - ballSize and ballY <= aiY + paddle_h and ballY >= aiY:
        ballSpeedX = -ballSpeedX

    # AI controls
    paddle_middle = aiY + paddle_h/2
    ball_middle = ballY + ballSize/2

    if ballX > 450:
        if paddle_middle - ball_middle > 200:
            aiY -= 2
        elif paddle_middle - ball_middle > 50:
            aiY -= 2
        elif paddle_middle - ball_middle < -200:
            aiY += 2
        elif paddle_middle - ball_middle < -50:
            aiY += 2
    elif ballX <= 450 and ballX > 150:
        if paddle_middle - ball_middle > 100:
            aiY -= 2
        elif paddle_middle - ball_middle < -100:
            aiY += 2

    ballX += ballSpeedX
    ballY += ballSpeedY

    drawPaddle(paddleX, paddleY, paddle_color)
    drawPaddle(aiX, aiY, ai_color)
    draw_score()
    drawBall(ballX, ballY)
    pygame.display.update()