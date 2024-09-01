import os
import pygame
import random
from pygame import mixer
import mysql.connector as ms
import sys

pygame.init()
clock=pygame.time.Clock()

screen=pygame.display.set_mode((650,500))

co=ms.connect(host='localhost',user='root',password="root",database="CB")
if co.is_connected():
    cu=co.cursor()
else:
    sys.exit()


pygame.display.set_caption("Chowka Bara")
icon=pygame.image.load("Asta Chamma-1.png")
pygame.display.set_icon(icon)
BoardImg=pygame.image.load("start game.png")
TitleImg=pygame.image.load("Asta Chamma-2.png")
exit=pygame.image.load("exit.png")
exit1=pygame.image.load("exit1.png")
next_button=pygame.image.load("next.png")
main_window=pygame.image.load("main window .png")

red_path={0:(400,50),1:(350,50),2:(300,50),3:(250,50),4:(250,100),5:(250,150),6:(250,200),7:(250,250),8:(250,300),9:(250,350),10:(300,350),11:(350,350),12:(400,350),13:(450,350),14:(500,350),15:(550,350),16:(550,300),17:(550,250),18:(550,200),19:(550,150),20:(550,100),21:(550,50),22:(500,50),23:(500,100),24:(500,150),25:(500,200),26:(500,250),27:(500,300),28:(450,300),29:(400,300),30:(350,300),31:(300,300),32:(300,250),33:(300,200),34:(300,150),35:(300,100),36:(350,100),37:(400,100),38:(450,100),39:(450,150),40:(450,200),41:(450,250),42:(400,250),43:(350,250),44:(350,200),45:(350,150),46:(400,150),47:(400,200),48:(70,400),49:(120,400),50:(170,400),51:(220,400)}

green_path={0:(400,350),1:(450,350),2:(500,350),3:(550,350),4:(550,300),5:(550,250),6:(550,200),7:(550,150),8:(550,100),9:(550,50),10:(500,50),11:(450,50),12:(400,50),13:(350,50),14:(300,50),15:(250,50),16:(250,100),17:(250,150),18:(250,200),19:(250,250),20:(250,300),21:(250,350),22:(300,350),23:(300,300),24:(300,250),25:(300,200),26:(300,150),27:(300,100),28:(350,100),29:(400,100),30:(450,100),31:(500,100),32:(500,150),33:(500,200),34:(500,250),35:(500,300),36:(450,300),37:(400,300),38:(350,300),39:(350,250),40:(350,200),41:(350,150),42:(400,150),43:(450,150),44:(450,200),45:(450,250),46:(400,250),47:(400,200),48:(400,400),49:(450,400),50:(500,400),51:(550,400)}

yellow_path={0:(250,200),1:(250,250),2:(250,300),3:(250,350),4:(300,350),5:(350,350),6:(400,350),7:(450,350),8:(500,350),9:(550,350),10:(550,300),11:(550,250),12:(550,200),13:(550,150),14:(550,100),15:(550,50),16:(500,50),17:(450,50),18:(400,50),19:(350,50),20:(300,50),21:(250,50),22:(250,100),23:(300,100),24:(350,100),25:(400,100),26:(450,100),27:(500,100),28:(500,150),29:(500,200),30:(500,250),31:(500,300),32:(450,300),33:(400,300),34:(350,300),35:(300,300),36:(300,250),37:(300,200),38:(300,150),39:(350,150),40:(400,150),41:(450,150),42:(450,200),43:(450,250),44:(400,250),45:(350,250),46:(350,200),47:(400,200), 48:(120,450),49:(170,450),50:(220,450),51:(270,450)}

blue_path={0:(550,200),1:(550,150),2:(550,100),3:(550,50),4:(500,50),5:(450,50),6:(400,50),7:(350,50),8:(300,50),9:(250,50),10:(250,100),11:(250,150),12:(250,200),13:(250,250),14:(250,300),15:(250,350),16:(300,350),17:(350,350),18:(400,350),19:(450,350),20:(500,350),21:(550,350),22:(550,300),23:(500,300),24:(450,300),25:(400,300),26:(350,300),27:(300,300),28:(300,250),29:(300,200),30:(300,150),31:(300,100),32:(350,100),33:(400,100),34:(450,100),35:(500,100),36:(500,150),37:(500,200),38:(500,250),39:(450,250),40:(400,250),41:(350,250),42:(350,200),43:(350,150),44:(400,150),45:(450,150),46:(450,200),47:(400,200),48:(380,450),49:(430,450),50:(480,450),51:(530,450)}

redplayerImg=pygame.image.load("red.png")
red_values=[red_1, red_2, red_3, red_4]=[0,0,0,0]

#Player green
greenplayerImg=pygame.image.load("green.png")
green_values=[green_1,green_2,green_3,green_4]=[0,0,0,0]

#Player yellow
yellowplayerImg=pygame.image.load("yellow.png")
yellow_values=[yellow_1,yellow_2,yellow_3,yellow_4]=[0,0,0,0]

#Player blue
blueplayerImg=pygame.image.load("blue.png")
blue_values=[blue_1,blue_2,blue_3,blue_4]=[0,0,0,0]

all=[0,0,0,0,0,0,00,0,0,0,0,0,0,0,0,0]

#Text box
tbd="Hi! Let's START THE GAME"
def text(x,dest,c=32,colour=(0,0,0)):
    font = pygame.font.Font('freesansbold.ttf', c)
    text = font.render(x,True,colour)
    screen.blit(text, dest)

#Name input
base_font = pygame.font.Font(None, 32)
user_text_red = ''
user_text_yellow = ''
user_text_green = ''
user_text_blue = ''
color_passive = pygame.Color((0,0,0))
color_red,color_yellow,color_green,color_blue = color_passive,color_passive,color_passive,color_passive
input_rect_red = pygame.Rect(50, 150, 200, 32)
input_rect_yellow = pygame.Rect(350, 150, 200, 32)
input_rect_green = pygame.Rect(50, 350, 200, 32)
input_rect_blue = pygame.Rect(350, 350, 200, 32)
active_green,active_yellow,active_blue,active_red = False,False,False,False
input_colour=[(255,0,0),(255,255,0),(0,255,0),(0,0,255)]

#Game loop
running=False
while not running:
    screen.fill((255,255,255))
    text("Enter your details",(170,10),40,(0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect_red.collidepoint(event.pos):
                active_red = True
                active_yellow=False
                active_green=False
                active_blue=False
            if input_rect_yellow.collidepoint(event.pos):
                active_yellow = True
                active_red = False
                active_green = False
                active_blue = False
            if input_rect_green.collidepoint(event.pos):
                active_green = True
                active_yellow = False
                active_red = False
                active_blue = False
            if input_rect_blue.collidepoint(event.pos):
                active_blue = True
                active_yellow = False
                active_red = False
                active_green = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if active_red:
                    user_text_red = user_text_red[:-1]
                if active_yellow:
                    user_text_yellow = user_text_yellow[:-1]
                if active_green:
                    user_text_green = user_text_green[:-1]
                if active_blue:
                    user_text_blue = user_text_blue[:-1]
            else:
                if active_red:
                    user_text_red += event.unicode
    #L=[user_text_red,user_text_yellow,user_text_green,user_text_blue]
    #print(L)
                if active_yellow:
                    user_text_yellow += event.unicode
                if active_green:
                    user_text_green += event.unicode
                if active_blue:
                    user_text_blue += event.unicode
    if active_red:
        color_red = input_colour[0]
    else:
        color_red = color_passive
    if active_yellow:
        color_yellow = input_colour[1]
    else:
        color_yellow = color_passive
    if active_green:
        color_green = input_colour[2]
    else:
        color_green = color_passive
    if active_blue:
        color_blue = input_colour[3]
    else:
        color_blue = color_passive
    text("Red",(100,100),32,(255,0,0))
    screen.blit(redplayerImg,(45,90))
    pygame.draw.rect(screen, color_red, input_rect_red)
    text_surface = base_font.render(user_text_red, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect_red.x, input_rect_red.y ))
    text("Yellow", (400, 100), 32, (255, 155, 100))
    screen.blit(yellowplayerImg, (350, 90))
    pygame.draw.rect(screen, color_yellow, input_rect_yellow)
    text_surface = base_font.render(user_text_yellow, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect_yellow.x, input_rect_yellow.y ))
    text("Green", (100, 300), 32, (0, 255, 0))
    screen.blit(greenplayerImg, (45, 285))
    pygame.draw.rect(screen, color_green, input_rect_green)
    text_surface = base_font.render(user_text_green, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect_green.x , input_rect_green.y))
    text("Blue", (400, 300), 32, (0, 0, 255))
    screen.blit(blueplayerImg, (350, 285))
    pygame.draw.rect(screen, color_blue, input_rect_blue)
    text_surface = base_font.render(user_text_blue, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect_blue.x , input_rect_blue.y))
    text("All the players have to write their name in",(30,440),28,(0,0,0))
    text("the respective boxes", (30, 470), 28, (0, 0, 0))
    screen.blit(next_button,(588,2))
    L=[user_text_red,user_text_yellow,user_text_green,user_text_blue]
    left, middle, right = pygame.mouse.get_pressed(3)
    if left:
        mouse = pygame.mouse.get_pos()
        mx, my = mouse
        mx, my = (mx // 50) * 50, (my // 50) * 50
        mouse = (mx, my)
    else:
        mouse = (0, 0)
    if mouse==(600,0):
        if user_text_red=='' or user_text_red.isdigit() or user_text_blue=='' or user_text_blue.isdigit() or user_text_yellow=='' or user_text_yellow.isdigit() or user_text_blue=='' or user_text_blue.isdigit():
            text("Please enter all the details",(50,410),32,(0,0,0))
        elif not ((user_text_red.isalpha()) and (user_text_yellow.isalpha()) and (user_text_green.isalpha()) and (user_text_blue.isalpha())):
            text("Only letters are allowed",(50,410),32,(0,0,0))
        elif len(user_text_red)>20 or len(user_text_yellow)>20 or len(user_text_green)>20 or len(user_text_blue)>20:
            text("Less than 20 charcters", (50, 410), 32, (0, 0, 0))
        else:
            user_text_red.lower()
            user_text_yellow.lower()
            user_text_green.lower()
            user_text_blue.lower()
            L = [user_text_red, user_text_yellow, user_text_green, user_text_blue]
            cu.execute("Select * from CB_Players")
            data=cu.fetchall()
            for i in data:
                if i[0] in L:
                    L.remove(i[0])
            for ele in L:
                cu.execute("insert into CB_Players values('{}',{},'{}')".format(ele,0,None))
                co.commit( )
    pygame.display.flip()
    clock.tick(60)
co.close()