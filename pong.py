from pygame import *
SCREENWIDTH = 900
SCREENHEIGHT = 600
screen = display.set_mode((SCREENWIDTH,SCREENHEIGHT))

font.init()
calibriBold35 = font.SysFont('Calibri Bold',35)

WHITE = (255, 255, 255)
BGCOLOR = (0, 220, 160)
BLUE = (50, 100, 230)
RED = (230, 50, 100)

p1Y = 250
p2Y = 250
paddleWidth = 30
paddleHeight = 100
p1Points = 0
p2Points = 0

ballX = 450
ballY = 300
ballDx = 4
ballDy = 4

running = True
myClock = time.Clock()
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    p1Paddle = Rect(50,p1Y,paddleWidth,paddleHeight)
    p2Paddle = Rect(850,p2Y,paddleWidth,paddleHeight)
    ball = Rect(ballX,ballY,10,10)
    keys = key.get_pressed()
    if(keys[K_w] and p1Y > 0):
        p1Y -= 5
    elif(keys[K_s] and p1Y + paddleHeight < SCREENHEIGHT):
        p1Y += 5
    if(keys[K_UP] and p2Y > 0):
        p2Y -= 5
    elif(keys[K_DOWN] and p2Y + paddleHeight < SCREENHEIGHT):
        p2Y += 5

    ballX += ballDx
    ballY += ballDy

    if(ball.colliderect(p1Paddle)):
        ballDx = abs(ballDx)
    elif(ball.colliderect(p2Paddle)):
        ballDx = -1*abs(ballDx)
    elif(ballY <= 0):
        ballDy = abs(ballDy)
    elif(ballY >= SCREENHEIGHT):
        ballDy = abs(ballDy)*-1

    if(ballX >= SCREENWIDTH or ballX <= 0):
        if(ballX >= SCREENWIDTH):
            p1Points += 1
        elif(ballX <= 0):
            p2Points += 1
        ballX = 450
        ballY = 300
        p1Y = 250
        p2Y = 250


    screen.fill(BGCOLOR)
    draw.rect(screen, BLUE, p1Paddle)
    draw.rect(screen, RED, p2Paddle)
    draw.rect(screen, WHITE, ball)
    p1PtsTxt = calibriBold35.render("P1 POINTS: " + str(p1Points),True, BLUE)
    p2PtsTxt = calibriBold35.render("P2 POINTS: " + str(p2Points),True, RED)
    screen.blit(p1PtsTxt,(130,20))
    screen.blit(p2PtsTxt,(620,20))
    display.flip()
    myClock.tick(60)
quit()
