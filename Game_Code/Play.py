#adding head

import pygame
import time
import random
#initialising pygame
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0, 155, 0)

display_width = 1200
display_height = 600

#this is display of the game
gameDisplay = pygame.display.set_mode((display_width,display_height))

#heading
pygame.display.set_caption('Slither')

icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon,)

img = pygame.image.load('snakeHead.png')
appleimg = pygame.image.load('apple.png')


clock = pygame.time.Clock()
AppleThickness = 30
block_size = 20
FPS = 15

direction = "up"

def snake(block_size, snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 40)
largefont = pygame.font.SysFont("comicsansms", 80)

def pause(score):
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        pause_score(score)
        message_to_screen("Paused",
                          green,
                          -60,
                          size="large")
        message_to_screen("Press C to continue or Q to quit",
                          black,
                          25)
        pygame.display.update()
        clock.tick(5)

def score(score):
    text = smallfont.render("Score: "+str(score),True,black)
    gameDisplay.blit(text,[0,0])


def final_score(score):
    text = largefont.render("Your Score: "+str(score),True,green)
    gameDisplay.blit(text,[350,100])

def pause_score(score):
    text = largefont.render("Current Score: "+str(score),True,green)
    gameDisplay.blit(text,[350,100])


def randAppleGen():
    randAppleX = round(random.randrange(0, display_width-AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-AppleThickness))#/10.0)*10.0
    return randAppleX,randAppleY



def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        
        
        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither",
                          green,
                          -100,
                          "large")
        message_to_screen("The objective of the game to eat apple",
                          black,
                          -30)
        message_to_screen("The more apples you eat the more you live",
                          black,
                          10)
        message_to_screen("If you run yourself or the edge , you die",
                          black,
                          50)
        message_to_screen("Press C to play,P to pause or press Q to exit",
                          black,
                          180)
        message_to_screen("Author :Manish Kumar Sinha",
                          green,
                          210)
        
        pygame.display.update()
        #clock.tick(2)



def text_objects(text,color,size):
    if size == "small":
        text_surface = smallfont.render(text, True,color)
    if size == "medium":
        text_surface = medfont.render(text, True,color)
    if size == "large":
        text_surface = largefont.render(text, True,color)
    return text_surface, text_surface.get_rect()

def message_to_screen(msg,color, y_displace=0,size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():

    
    global direction
    direction = "up"
    gameExit = False
    gameOver = False

    #snakeList is declared here bcz it will help in lengthening the snake
    snakeList = []
    snakeLength = 1

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    
    #rounding appple position in multiple of 10
    randAppleX,randAppleY = randAppleGen()
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            
            message_to_screen("Game over",
                              red,
                              -50,
                              size = "large")
            final_score(snakeLength-1)
            message_to_screen(" Press c to play again or q to exit",
                              black,
                              70,
                              size="medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameExit = True
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                                direction="left"
                                lead_x_change = -block_size
                                lead_y_change = 0
                        elif event.key == pygame.K_RIGHT:
                                direction="right"
                                lead_x_change = block_size
                                lead_y_change = 0
                        elif event.key == pygame.K_UP:
                                direction="up"
                                lead_y_change = -block_size
                                lead_x_change = 0
                        elif event.key == pygame.K_DOWN:
                                direction="down"
                                lead_y_change = block_size
                                lead_x_change = 0
                        elif event.key == pygame.K_p:
                                pause(snakeLength-1)
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
                        gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        #for apples

        
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness,AppleThickness])


        #for snake

        
        snakeHead= []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        #without this snake will get lengthen and lengthen
        if len(snakeList) > snakeLength:
            del snakeList[0]
        #for self attaking
        for eachSegment in snakeList[:-1]:  #each element upto last(except last)
                if eachSegment == snakeHead:
                    gameOver = True
        
        snake(block_size, snakeList)

        score(snakeLength-1)
        
        pygame.display.update()


##        if lead_x >= randAppleX and lead_x < randAppleX + AppleThickness:
##            if lead_y >= randAppleY and lead_y < randAppleY + AppleThickness:
##                randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
##                randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
##                snakeLength += 1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1
        clock.tick(FPS)
    #uninitialising  pygame
    pygame.quit()
    quit()

game_intro()
gameLoop()
