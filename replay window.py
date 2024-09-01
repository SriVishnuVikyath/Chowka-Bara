import csv
import os
import time
import pygame
import random
from pygame import mixer
import mysql.connector as ms
import sys

pygame.init()
clock=pygame.time.Clock()

co=ms.connect(host='localhost',user='root',password="root",database='CB')
if co.is_connected():
    cu=co.cursor()
else:
    sys.exit()
try:
    cu.execute('create table CB_Plays(Red_Player char(20),Yellow_Player char(20),Green_Player char(20),Blue_Player char(20),History varchar(200))')
    co.commit()
except:
    print('database connected')

screen=pygame.display.set_mode((650,500))

pygame.display.set_caption("Chowka Bara")
icon=pygame.image.load("Asta Chamma-1.png")
pygame.display.set_icon(icon)
BoardImg=pygame.image.load("Asta Chamma-1.png")
TitleImg=pygame.image.load("Asta Chamma-2.png")
exit=pygame.image.load("exit.png")
exit1=pygame.image.load("exit1.png")
next_button=pygame.image.load("next.png")
main_window=pygame.image.load("main window .png")
do=pygame.image.load('do.png')

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
def text(x,dest=(250,10),c=32,colour=(0,0,0)):
    font = pygame.font.Font('freesansbold.ttf', c)
    text = font.render(x,True,colour)
    screen.blit(text, dest)

#Bgcolour
colour=(255, 235, 205)
colours=((238,70,70),(255,234,0),(0,255,0),(0,200,255))
text_colour=(0,0,0)
text_colours=((0,0,0),(191,64,191),(0,0,0),(245,245,220))

#Players
Players=("Red","Yellow","Green","Blue")
all=[red_1, yellow_1, green_1, blue_1, red_2, yellow_2, green_2, blue_2, red_3, yellow_3, green_3, blue_3, red_4,yellow_4, green_4, blue_4]
Chance = 0
last_played=None
end_value=[48,49,50,51]

#Dice(Kavade)
dice_value = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 8]
dice_state="ready"
dice_type='kavade'
def indice(x,y):
  infacediceImg=pygame.image.load("indice.png")
  screen.blit(infacediceImg,(x,y))
def outdice(x,y):
  outfacediceImg=pygame.image.load("outdice.png")
  screen.blit(outfacediceImg,(x,y))
dice_output=0
def kavade():
    if dice_output == 1:
        indice(25, 225)
        outdice(25, 325)
        outdice(125, 225)
        outdice(125, 325)
        tbd = "1"
    elif dice_output == 2:
        indice(25, 225)
        indice(25, 325)
        outdice(125, 225)
        outdice(125, 325)
        tbd = "2"
    elif dice_output == 3:
        indice(25, 225)
        indice(25, 325)
        indice(125, 225)
        outdice(125, 325)
        tbd = "3"
    elif dice_output == 4:
        indice(25, 225)
        indice(25, 325)
        indice(125, 225)
        indice(125, 325)
        tbd = "4"
    elif dice_output == 8:
        outdice(25, 225)
        outdice(25, 325)
        outdice(125, 225)
        outdice(125, 325)
        tbd = "8"
def dice():
    if dice_output==1:
        screen.blit(pygame.image.load('dice 1.png'),(25,225))
        tbd="1"
    elif dice_output==2:
        screen.blit(pygame.image.load('dice 2.png'),(25,225))
        tbd="2"
    elif dice_output==3:
        screen.blit(pygame.image.load('dice 3.png'),(25,225))
        tbd="3"
    elif dice_output==4:
        screen.blit(pygame.image.load('dice 4.png'),(25,225))
        tbd="4"
    elif dice_output==8:
        screen.blit(pygame.image.load('dice 8.jpg'),(25,225))
        tbd="8"

other_info = [last_played, dice_output, Chance, dice_state, dice_type]

#file object
fname='Sample Run'
f=open("{}.csv".format(fname),'r')
fr=csv.reader(f)
game_state='Replay Window'

#Replay Screen
replay_screen=0
table=[]

#while
running=False
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=True
    if game_state!='Replay Window':
        running=True
    screen.fill((255, 255, 255))
    screen.blit(next_button, (580, 20))
    screen.blit(pygame.transform.rotate(next_button, 180), (10, 10))
    screen.blit(next_button, (480, 440))
    text('Want to Start a new game?',(50,460),32,(0,255,100))
    [red_1, yellow_1, green_1, blue_1, red_2, yellow_2, green_2, blue_2, red_3, yellow_3, green_3, blue_3, red_4,
     yellow_4, green_4, blue_4] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    left, middle, right = pygame.mouse.get_pressed(3)
    if left:
        mouse = pygame.mouse.get_pos()
        mx, my = mouse
        mx, my = (mx // 50) * 50, (my // 50) * 50
        mouse = (mx, my)
        print(mouse)
    else:
        mouse = (0, 0)
    if mouse[0] >= 580 and mouse[1] <= 60:
        if len(table)<2:
            replay_screen=1
        else:
            replay_screen += 1
    if mouse[0] <= 60 and mouse[1] <= 60 and left:
        if replay_screen!=0:
            replay_screen-= 1
        else:
            replay_screen=0
    if mouse[0] in (450,500) and mouse[1] in (400,450):
        game_state='Started'
        red_values = [red_1, red_2, red_3, red_4] = [0, 0, 0, 0]
        green_values = [green_1, green_2, green_3, green_4] = [0, 0, 0, 0]
        yellow_values = [yellow_1, yellow_2, yellow_3, yellow_4] = [0, 0, 0, 0]
        blue_values = [blue_1, blue_2, blue_3, blue_4] = [0, 0, 0, 0]
        all=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        Chance = 0
        last_played = None
        cu.execute('select sysdate()')
        dt_time = cu.fetchone()
        dt = str(dt_time)
        print(dt)
        dtt = dt.replace(', ','')
        fname = dtt[19:-3]
        f = open("{}.csv".format(fname), 'w', newline='')
        f.close()
        fi = 'do not delete'
        other_info = [last_played, dice_output, Chance, dice_state, dice_type]
        filename = None
        on_screen = 0
        user_text_red = ''
        user_text_yellow = ''
        user_text_green = ''
        user_text_blue = ''
        active_green, active_yellow, active_blue, active_red = False, False, False, False
        winner = None
        insert_count = 0
    if replay_screen!=0:
        cu.execute('Select * from CB_Plays')
        for i in range(0,replay_screen):
            table = cu.fetchmany(2)
        text('PLAYERS',(15,80))
        text('REPLAY BUTTON',(190,80))
        text('DATE', (480, 80))
        if len(table)==1 or len(table)==2:
            text(table[0][0],(15,140),20)
            text(table[0][1], (15, 170),20)
            text(table[0][2], (15, 200), 20)
            text(table[0][3], (15, 230), 20)
            screen.blit(next_button, (250, 150))
            text(str(table[0][5]), (480, 170), 20)
        if len(table)==2:
            text(table[1][0], (15, 270), 20)
            text(table[1][1], (15, 300), 20)
            text(table[1][2], (15, 330), 20)
            text(table[1][3], (15, 360), 20)
            screen.blit(next_button, (250, 350))
            text(str(table[0][5]), (480, 170), 20)
    else:
        text('Your Play has been recorded', (100, 20), 30)
        text('Do you want to watch the replay', (10,180),40)
        screen.blit(next_button,(300,250))
        if mouse[0] in (300, 350) and mouse[1] in (250, 300):
            game_state='Replay'
            filename=fname
    pygame.display.flip()
    clock.tick(20)
co.close()
print('database disconnected')