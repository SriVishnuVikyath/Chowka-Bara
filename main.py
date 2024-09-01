import csv
import os
import time
import moviepy.editor
import pygame
import random
from pygame import mixer
import mysql.connector as ms
import sys
from datetime import date

pygame.init()
clock=pygame.time.Clock()

video = moviepy.editor.VideoFileClip("opening video.mp4")
video.preview()
screen=pygame.display.set_mode((650,500))

co=ms.connect(host='localhost',user='root',password="root",database='CB')
if co.is_connected():
    cu=co.cursor()
else:
    sys.exit()

try:
    cu.execute('create table CB_Plays(Red_Player char(20),Yellow_Player char(20),Green_Player char(20),Blue_Player char(20),History varchar(200),Date_Played date)')
    co.commit()
except:
    print('database connected')

pygame.display.set_caption("Chowka Bara")
icon=pygame.image.load("Asta Chamma-1.png")
pygame.display.set_icon(icon)
BoardImg=pygame.image.load("Asta Chamma-1.png")
TitleImg=pygame.image.load("start game.png")
exit=pygame.image.load("exit.png")
exit1=pygame.image.load("exit1.png")
next_button=pygame.image.load("next.png")
main_window=pygame.image.load("main window .png")
do=pygame.image.load('do.png')
dice_type_select=pygame.image.load('kavade.dice.png')

red_path={0:(400,50),1:(350,50),2:(300,50),3:(250,50),4:(250,100),5:(250,150),6:(250,200),7:(250,250),8:(250,300),9:(250,350),10:(300,350),11:(350,350),12:(400,350),13:(450,350),14:(500,350),15:(550,350),16:(550,300),17:(550,250),18:(550,200),19:(550,150),20:(550,100),21:(550,50),22:(500,50),23:(500,100),24:(500,150),25:(500,200),26:(500,250),27:(500,300),28:(450,300),29:(400,300),30:(350,300),31:(300,300),32:(300,250),33:(300,200),34:(300,150),35:(300,100),36:(350,100),37:(400,100),38:(450,100),39:(450,150),40:(450,200),41:(450,250),42:(400,250),43:(350,250),44:(350,200),45:(350,150),46:(400,150),47:(400,200),48:(70,400),49:(120,400),50:(170,400),51:(220,400)}

green_path={0:(400,350),1:(450,350),2:(500,350),3:(550,350),4:(550,300),5:(550,250),6:(550,200),7:(550,150),8:(550,100),9:(550,50),10:(500,50),11:(450,50),12:(400,50),13:(350,50),14:(300,50),15:(250,50),16:(250,100),17:(250,150),18:(250,200),19:(250,250),20:(250,300),21:(250,350),22:(300,350),23:(300,300),24:(300,250),25:(300,200),26:(300,150),27:(300,100),28:(350,100),29:(400,100),30:(450,100),31:(500,100),32:(500,150),33:(500,200),34:(500,250),35:(500,300),36:(450,300),37:(400,300),38:(350,300),39:(350,250),40:(350,200),41:(350,150),42:(400,150),43:(450,150),44:(450,200),45:(450,250),46:(400,250),47:(400,200),48:(400,400),49:(450,400),50:(500,400),51:(550,400)}

yellow_path={0:(250,200),1:(250,250),2:(250,300),3:(250,350),4:(300,350),5:(350,350),6:(400,350),7:(450,350),8:(500,350),9:(550,350),10:(550,300),11:(550,250),12:(550,200),13:(550,150),14:(550,100),15:(550,50),16:(500,50),17:(450,50),18:(400,50),19:(350,50),20:(300,50),21:(250,50),22:(250,100),23:(300,100),24:(350,100),25:(400,100),26:(450,100),27:(500,100),28:(500,150),29:(500,200),30:(500,250),31:(500,300),32:(450,300),33:(400,300),34:(350,300),35:(300,300),36:(300,250),37:(300,200),38:(300,150),39:(350,150),40:(400,150),41:(450,150),42:(450,200),43:(450,250),44:(400,250),45:(350,250),46:(350,200),47:(400,200), 48:(120,450),49:(170,450),50:(220,450),51:(270,450)}

blue_path={0:(550,200),1:(550,150),2:(550,100),3:(550,50),4:(500,50),5:(450,50),6:(400,50),7:(350,50),8:(300,50),9:(250,50),10:(250,100),11:(250,150),12:(250,200),13:(250,250),14:(250,300),15:(250,350),16:(300,350),17:(350,350),18:(400,350),19:(450,350),20:(500,350),21:(550,350),22:(550,300),23:(500,300),24:(450,300),25:(400,300),26:(350,300),27:(300,300),28:(300,250),29:(300,200),30:(300,150),31:(300,100),32:(350,100),33:(400,100),34:(450,100),35:(500,100),36:(500,150),37:(500,200),38:(500,250),39:(450,250),40:(400,250),41:(350,250),42:(350,200),43:(350,150),44:(400,150),45:(450,150),46:(450,200),47:(400,200),48:(380,450),49:(430,450),50:(480,450),51:(530,450)}

safe_path=((400,50),(400,350),(250,200),(550,200),(300,100),(500,100),(300,300),(500,300))

#Player Red
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

#Text box
tbd="Hi! Let's START THE GAME"
def text(x,dest=(250,10),FONT=32,colour=(0,0,0)):
    font = pygame.font.Font('freesansbold.ttf', FONT)
    text = font.render(x,True,colour)
    screen.blit(text, dest)

#Dice(Kavade)
dice_value = (1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 8)
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

#Players
Players=("Red","Yellow","Green","Blue")
all=[red_1, yellow_1, green_1, blue_1, red_2, yellow_2, green_2, blue_2, red_3, yellow_3, green_3, blue_3, red_4,yellow_4, green_4, blue_4]
Chance = 0
last_played=None
end_value=[48,49,50,51]

#Music
musics=('background.wav','game run.mp3','Killing rolex.mp3')
music=0
volume=0.5
mixer.music.load(musics[music])
mixer.music.play(-1)
mixer.music.set_volume(volume)

#File object
today=date.today()
print(today)
today_int=random.randint(0,100000)
fname= str(today) + str(today_int)
fname=fname.replace('-','')
f = open("{}.csv".format(fname), 'w',newline='')
f.close()
other_info=[last_played,dice_output,Chance,dice_state,dice_type]
filename=None
f=open('{}.csv'.format(fname),'w',newline='')
f.close()

#Bgcolour
colour=(255, 235, 205)
colours=((238,70,70),(255,234,0),(0,255,0),(0,200,255))
text_colour=(0,0,0)
text_colours=((0,0,0),(191,64,191),(0,0,0),(245,245,220))

#Info pages
on_screen=0
def line(line_no):
    with open('CB.txt',newline='\n') as ft:
        full_file=ft.readlines()
        line=full_file[line_no-1]
        line=str(line)
    return line

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

#winner
winner=None
redwin = moviepy.editor.VideoFileClip("red-winner.mp4")
yellowwin = moviepy.editor.VideoFileClip("yellow-winner.mp4")
greenwin = moviepy.editor.VideoFileClip("green-winner.mp4")
bluewin = moviepy.editor.VideoFileClip("blue-winner.mp4")

#Replay Screen
replay_screen=1
table=[]
insert_count=0
replay_count=0
replay_list=[]
table_count=0

#Game loop
running=False
game_state='Replay window'
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if game_state=='Playing':
              game_state='Replay Window'
            else:
                running=True
    if game_state=='Started':
        screen.fill((0, 0, 0))
        screen.blit(main_window,(0,0))
        screen.blit(next_button,(500,440))
        left, middle, right = pygame.mouse.get_pressed(3)
        if left:
            mouse = pygame.mouse.get_pos()
            mx, my = mouse
            mx, my = (mx // 50) * 50, (my // 50) * 50
            mouse = (mx, my)
            print(mouse)
        else:
            mouse = (0, 0)
        if mouse[0] >= 200 and mouse[0] <= 400 and mouse[1] >= 150 and mouse[1] <= 200:
            game_state = 'Name Input'
        text("Click here to get to know about the game rules",(0,460),22,(255,255,255))
        text("Go to replay menu window", (100, 430), 22, (255, 255, 255))
        screen.blit(next_button, (390, 400))
        if mouse[0] in (450,500) and mouse[1] in (450,500):
            game_state='Info'
        if mouse[0] in (400,450) and mouse[1] in (450,400):
            game_state='Replay window'
        if (mouse[0] in (250,300,350)) and (mouse[1] in (250,300)):
            os.remove('{}.csv'.format(fname))
            running=True
    if game_state=='Name Input':
        screen.fill((255, 255, 255))
        text("Enter your details", (170, 10), 40, (0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect_red.collidepoint(event.pos):
                    active_red = True
                    active_yellow = False
                    active_green = False
                    active_blue = False
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
        text("Red", (100, 100), 32, (255, 0, 0))
        screen.blit(redplayerImg, (45, 90))
        pygame.draw.rect(screen, color_red, input_rect_red)
        text_surface = base_font.render(user_text_red, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect_red.x, input_rect_red.y))
        text("Yellow", (400, 100), 32, (255, 155, 100))
        screen.blit(yellowplayerImg, (350, 90))
        pygame.draw.rect(screen, color_yellow, input_rect_yellow)
        text_surface = base_font.render(user_text_yellow, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect_yellow.x, input_rect_yellow.y))
        text("Green", (100, 300), 32, (0, 255, 0))
        screen.blit(greenplayerImg, (45, 285))
        pygame.draw.rect(screen, color_green, input_rect_green)
        text_surface = base_font.render(user_text_green, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect_green.x, input_rect_green.y))
        text("Blue", (400, 300), 32, (0, 0, 255))
        screen.blit(blueplayerImg, (350, 285))
        pygame.draw.rect(screen, color_blue, input_rect_blue)
        text_surface = base_font.render(user_text_blue, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect_blue.x, input_rect_blue.y))
        text("All the players have to write their name in", (30, 440), 28, (0, 0, 0))
        text("the respective boxes", (30, 470), 28, (0, 0, 0))
        screen.blit(next_button, (588, 2))
        L = [user_text_red, user_text_yellow, user_text_green, user_text_blue]
        left, middle, right = pygame.mouse.get_pressed(3)
        if left:
            mouse = pygame.mouse.get_pos()
            mx, my = mouse
            mx, my = (mx // 50) * 50, (my // 50) * 50
            mouse = (mx, my)
        else:
            mouse = (0, 0)
        if mouse == (600, 0):
            if user_text_red == '' or user_text_red.isdigit() or user_text_blue == '' or user_text_blue.isdigit() or user_text_yellow == '' or user_text_yellow.isdigit() or user_text_blue == '' or user_text_blue.isdigit():
                text("Please enter all the details", (50, 410), 32, (0, 0, 0))
            elif not ((user_text_red.isalpha()) and (user_text_yellow.isalpha()) and (user_text_green.isalpha()) and (user_text_blue.isalpha())):
                text("Only letters are allowed", (50, 410), 32, (0, 0, 0))
            elif len(user_text_red) > 20 or len(user_text_yellow) > 20 or len(user_text_green) > 20 or len(user_text_blue) > 20:
                text("Less than 20 charcters", (50, 410), 32, (0, 0, 0))
            else:
                user_text_red.lower()
                user_text_yellow.lower()
                user_text_green.lower()
                user_text_blue.lower()
                cu.execute("Select * from CB_Plays")
                data = cu.fetchall()
                filename='{}.csv'.format(fname)
                cu.execute("insert into CB_Plays values('{}','{}','{}','{}','{}','{}')".format(user_text_red,user_text_yellow,user_text_green,user_text_blue,filename,today))
                co.commit()
                game_state='Dice'
                filename = None
                user_text_red, user_text_yellow, user_text_green, user_text_blue = None,None,None,None
                active_green, active_yellow, active_blue, active_red = False, False, False, False
            clock.tick(30)
    if game_state=='Dice':
        screen.fill((colour))
        left, middle, right = pygame.mouse.get_pressed(3)
        screen.blit(dice_type_select, (0, 100))
        text('What type of Dice do you want?', (100, 40),32,(255,0,100))
        if left:
            mouse = pygame.mouse.get_pos()
            if mouse[1]>=130 and mouse[1]<=350:
                if mouse[0]<=335:
                    dice_type='dice'
                else:
                    dice_type='kavade'
                game_state='Playing'
    if game_state=='Info':
        screen.fill((colour))
        screen.blit(next_button, (580, 10))
        screen.blit(pygame.transform.rotate(next_button,180),(10,10))
        screen.blit(exit1, (580, 450))
        left, middle, right = pygame.mouse.get_pressed(3)
        if left:
            mouse = pygame.mouse.get_pos()
            mx, my = mouse
            mx, my = (mx // 50) * 50, (my // 50) * 50
            mouse = (mx, my)
            time.sleep(0.1)
        else:
            mouse = (0, 0)
        if mouse[0] >= 580 and mouse[1] >= 450:
                running=True
                os.remove('{}.csv'.format(fname))
        if mouse[0]>=580 and mouse[1]<=60:
            on_screen+=1
            if on_screen==4:
                game_state = 'Name Input'
                on_screen = 0
        if mouse[0]<=60 and mouse[1]<=60 and mouse!=(0,0):
            on_screen-=1
            if on_screen<0:
                game_state = 'Started'
        if on_screen==0:
            text('Info',(270, 15), 60, (0, 0, 0))
            screen.blit(BoardImg, (150, 130))
            text(line(1), (15,80), 21, (200, 100, 0))
            text(line(2), (15,105), 21, (200, 100, 0))
        elif on_screen==1:
            for i in range(3, 13):
                text(line(i), (5, 40 * i - 40), 32, (200, 100, 0))
        elif on_screen == 2:
            text('Rules', (235, 15), 60, (0, 0, 0))
            for i in range(13, 25):
                text(line(i), (5, 30 * i - 280), 21, (200, 100, 0))
        elif on_screen == 3:
            text('Guidelines', (185, 15), 60, (0, 0, 0))
            for i in range(24, 31):
                text(line(i), (5, 40 * i - 880), 21, (200, 100, 0))
    if game_state=='Playing':
        screen.fill((colour))
        screen.blit(BoardImg, (250, 50))
        screen.blit(TitleImg, (25, 50))
        screen.blit(redplayerImg, red_path[red_1])
        screen.blit(redplayerImg, red_path[red_2])
        screen.blit(redplayerImg, red_path[red_3])
        screen.blit(redplayerImg, red_path[red_4])
        screen.blit(greenplayerImg, green_path[green_1])
        screen.blit(greenplayerImg, green_path[green_2])
        screen.blit(greenplayerImg, green_path[green_3])
        screen.blit(greenplayerImg, green_path[green_4])
        screen.blit(blueplayerImg, blue_path[blue_1])
        screen.blit(blueplayerImg, blue_path[blue_2])
        screen.blit(blueplayerImg, blue_path[blue_3])
        screen.blit(blueplayerImg, blue_path[blue_4])
        screen.blit(yellowplayerImg, yellow_path[yellow_1])
        screen.blit(yellowplayerImg, yellow_path[yellow_2])
        screen.blit(yellowplayerImg, yellow_path[yellow_3])
        screen.blit(yellowplayerImg, yellow_path[yellow_4])
        text(tbd,(250,10),32,text_colour)
        Chance = Chance % 4
        if dice_state=="ready":
            tbd="It's "+str(Players[Chance])+" Chance"
        if dice_state=="ready" or dice_state=="value":
            colour=colours[Chance]
            text_colour=text_colours[Chance]
        else:
            colour=(255, 235, 205)
            text_colour=(0,0,0)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and dice_state=="ready":
                    val = random.randint(0,22)
                    dice_output = dice_value[val]
                    dice_state = "value"
                    print(all)
                    other_info = [last_played, dice_output, Chance, dice_state, dice_type]
                    print(other_info)
                    insert_count+=1
                    with open('{}.csv'.format(fname),'a+',newline='') as f:
                        fw=csv.writer(f)
                        fw.writerow(all)
                        fw.writerow(other_info)
        left,middle,right=pygame.mouse.get_pressed(3)
        if left:
            mouse=pygame.mouse.get_pos()
            mx, my = mouse
            mx, my = (mx // 50) * 50, (my // 50) * 50
            mouse = (mx, my)
        else:
            mouse=(0,0)
        if dice_state=="value":
            if dice_type=='dice':
                dice()
            else:
                kavade()
        if dice_state=='value':
            if Chance==0 :
                for i in range(0,16,4):
                    if  red_path[all[i]]==mouse:
                        if all[i]+dice_output>47:
                            Chance+=1
                        elif dice_output>=4:
                            all[i]+=dice_output
                        else:
                            all[i]+=dice_output
                            Chance+=1
                        dice_state='ready'
                        last_played='Red'
                        break
            elif Chance == 1:
                for i in range(1, 16, 4):
                    if yellow_path[all[i]] == mouse:
                        if all[i]+dice_output>47:
                            Chance+=1
                        elif dice_output>=4:
                            all[i]+=dice_output
                        else:
                            all[i]+=dice_output
                            Chance+=1
                        dice_state='ready'
                        last_played = 'Yellow'
                        break
            elif Chance == 2:
                for i in range(2, 16, 4):
                    if green_path[all[i]] == mouse:
                        if all[i]+dice_output>47:
                            Chance+=1
                        elif dice_output>=4:
                            all[i]+=dice_output
                        else:
                            all[i]+=dice_output
                            Chance+=1
                        dice_state='ready'
                        last_played = 'Green'
                        break
            elif Chance == 3:
                for i in range(3, 16, 4):
                    if blue_path[all[i]] == mouse:
                        if all[i]+dice_output>47:
                            Chance+=1
                        elif dice_output>=4:
                            all[i]+=dice_output
                        else:
                            all[i]+=dice_output
                            Chance+=1
                        dice_state='ready'
                        last_played = 'Blue'
                        break
        [red_1, yellow_1, green_1, blue_1, red_2, yellow_2, green_2, blue_2, red_3, yellow_3, green_3, blue_3, red_4,yellow_4, green_4, blue_4] = all
        for i in range(4):
            red_values[i]=all[4*i]
            yellow_values[i]=all[4*i+1]
            green_values[i]=all[4*i+2]
            blue_values[i]=all[4*i+3]
        if last_played=='Red':
            for i in range(4):
                for j in range (4):
                    if red_path[red_values[i]]==yellow_path[yellow_values[j]] and yellow_path[yellow_values[j]] not in safe_path:
                        yellow_values[j]=0
                        Chance=0
                    elif red_path[red_values[i]]==green_path[green_values[j]] and green_path[green_values[j]] not in safe_path:
                        green_values[j]=0
                        Chance=0
                    elif red_path[red_values[i]]==blue_path[blue_values[j]] and blue_path[blue_values[j]] not in safe_path:
                        blue_values[j]=0
                        Chance=0
        elif last_played=='Yellow':
            for i in range(4):
                for j in range(4):
                    if yellow_path[yellow_values[i]]==red_path[red_values[j]] and red_path[red_values[j]] not in safe_path:
                        red_values[j]=0
                        Chance=1
                    elif yellow_path[yellow_values[i]]==green_path[green_values[j]] and green_path[green_values[j]] not in safe_path:
                        green_values[j]=0
                        Chance=1
                    elif yellow_path[yellow_values[i]]==blue_path[blue_values[j]] and blue_path[blue_values[j]] not in safe_path:
                        blue_values[j]=0
                        Chance=1
        elif last_played=='Green':
            for i in range(4):
                for j in range(4):
                    if green_path[green_values[i]]==red_path[red_values[j]] and red_path[red_values[j]] not in safe_path:
                        red_values[j]=0
                        Chance=2
                    elif green_path[green_values[i]]==yellow_path[yellow_values[j]] and yellow_path[yellow_values[j]] not in safe_path:
                        yellow_values[j]=0
                        Chance=2
                    elif green_path[green_values[i]]==blue_path[blue_values[j]] and blue_path[blue_values[j]] not in safe_path:
                        blue_values[j]=0
                        Chance=2
        elif last_played=='Blue':
            for i in range(4):
                for j in range(4):
                    if blue_path[blue_values[i]]==red_path[red_values[j]] and red_path[red_values[j]] not in safe_path:
                        red_values[j]=0
                        Chance=3
                    elif blue_path[blue_values[i]]==yellow_path[yellow_values[j]] and yellow_path[yellow_values[j]] not in safe_path:
                        yellow_values[j]=0
                        Chance=3
                    elif blue_path[blue_values[i]]==green_path[green_values[j]] and green_path[green_values[j]] not in safe_path:
                        green_values[j]=0
                        Chance=3
        for i in range(4):
            all[4*i]=red_values[i]
            all[4*i+1]=yellow_values[i]
            all[4*i+2]=green_values[i]
            all[4*i+3]=blue_values[i]
        for i in range(0,16):
            if all[i]>=47:
                j=i//4
                all[i]=end_value[j]
        for i in range(4):
            red_values[i]=all[4*i]
            yellow_values[i]=all[4*i+1]
            green_values[i]=all[4*i+2]
            blue_values[i]=all[4*i+3]
        text("Red",(10,410),25,text_colour)
        text("Yellow",(10,460),25,text_colour)
        text("Green",(325,410),25,text_colour)
        text("Blue",(325,460),25,text_colour)
        screen.blit(exit1,(580,450))
        other_info = [last_played, dice_output,Chance,dice_state,dice_type]
        if (red_values==end_value):
            winner='Red'
        if (yellow_values==end_value):
            winner='Yellow'
        if (green_values==end_value):
            winner='Green'
        if (blue_values==end_value):
            winner='Blue'
        if (mouse[0] >= 580 and mouse[1] >= 450):
            game_state='Replay Window'
            other_info = []  # Emptying all the unwanted variables
            red_values = [red_1, red_2, red_3, red_4] = [0, 0, 0, 0]
            green_values = [green_1, green_2, green_3, green_4] = [0, 0, 0, 0]
            yellow_values = [yellow_1, yellow_2, yellow_3, yellow_4] = [0, 0, 0, 0]
            blue_values = [blue_1, blue_2, blue_3, blue_4] = [0, 0, 0, 0]
            all = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            Chance = 0
            last_played = None
            dice_output = 0
            dice_type = None
            insert_count = 0
            filename = '{}.csv'.format(fname)
            cu.execute('delete from CB_Plays where History={}'.format(filename))
            co.commit()
            filename=None
        if winner!=None:
            game_state='Winner'
            with open('{}.csv'.format(fname), 'a+', newline='') as f:
                fw = csv.writer(f)
                fw.writerow([winner,'Eof','','','','','','','','','','','','','','',''])
            other_info=[]#Emptying all the unwanted variables
            red_values = [red_1, red_2, red_3, red_4] = [0, 0, 0, 0]
            green_values = [green_1, green_2, green_3, green_4] = [0, 0, 0, 0]
            yellow_values = [yellow_1, yellow_2, yellow_3, yellow_4] = [0, 0, 0, 0]
            blue_values = [blue_1, blue_2, blue_3, blue_4] = [0, 0, 0, 0]
            all=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            Chance = 0
            last_played = None
            dice_output = 0
            dice_type = None
            replay_screen=0
    if game_state=='Winner':
        if winner=='Red':
            redwin.preview()
        elif winner=='Yellow':
            yellowwin.preview()
        elif winner=='Green':
            greenwin.preview()
        elif winner=='Blue':
            bluewin.preview()
        game_state = 'Replay window'
        winner = None
    if game_state=='Replay window':
        screen.fill((255, 255, 255))
        screen.blit(next_button, (580, 20))
        screen.blit(pygame.transform.rotate(next_button, 180), (10, 10))
        screen.blit(next_button, (480, 440))
        text('Want to Start a new game?', (50, 460), 32, (0, 255, 100))
        [red_1, yellow_1, green_1, blue_1, red_2, yellow_2, green_2, blue_2, red_3, yellow_3, green_3, blue_3, red_4,
         yellow_4, green_4, blue_4] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        left, middle, right = pygame.mouse.get_pressed(3)
        if left:
            mouse = pygame.mouse.get_pos()
            mx, my = mouse
            mx, my = (mx // 50) * 50, (my // 50) * 50
            mouse = (mx, my)
            time.sleep(0.3)
            print(table_count,replay_screen)
        else:
            mouse = (0, 0)
        if mouse[0] >= 580 and mouse[1] <= 60:
            table_count+=2
            if len(main_table) <= table_count:
                table_count=len(main_table)-1
            else:
                replay_screen += 1
        if mouse[0] <= 60 and mouse[1] <= 60 and left:
            table_count-=2
            if table_count<0:
                table_count=0
                replay_screen = 0
            else:
                replay_screen -=1
        if mouse[0] in (450, 500) and mouse[1] in (400, 450):
            game_state = 'Started'
            today = date.today()
            print(today)
            today_int = random.randint(0, 10000)
            fname = str(today) + str(today_int)
            fname = fname.replace('-', '')
            f = open("{}.csv".format(fname), 'w', newline='')
            f.close()
            insert_count=0
        screen.blit(exit1, (580, 450))
        if (mouse[0] >= 580 and mouse[1] >= 450):
            running=True
        cu.execute('select * from CB_Plays')
        main_table = cu.fetchall()
        co.commit()
        if replay_screen != 0:
            text('PLAYERS', (15, 80))
            text('REPLAY BUTTON', (190, 80))
            text('DATE', (480, 80))
            if not (len(main_table)-table_count)<2:
                table.append(main_table[table_count])
                table.append(main_table[table_count+1])
                text(table[0][0], (15, 140), 20)
                text(table[0][1], (15, 170), 20)
                text(table[0][2], (15, 200), 20)
                text(table[0][3], (15, 230), 20)
                screen.blit(next_button, (250, 150))
                if mouse[0] in (250,300) and mouse[1] in (150,200):
                    game_state='Replay'
                    filename=str(table[0][4])
                    with open(filename,'r') as file:
                        fr=csv.reader(file)
                        for rec in fr:
                            replay_list.append(rec)
                text(str(table[0][5]), (480, 170), 20)
                text(table[1][0], (15, 270), 20)
                text(table[1][1], (15, 300), 20)
                text(table[1][2], (15, 330), 20)
                text(table[1][3], (15, 360), 20)
                screen.blit(next_button, (250, 350))
                if mouse[0] in (250,300) and mouse[1] in (350,400):
                    game_state='Replay'
                    filename=str(table[1][4])
                    with open(filename,'r') as file:
                        fr=csv.reader(file)
                        for rec in fr:
                            replay_list.append(rec)
                text(str(table[1][5]), (480, 170), 20)
                table = []
            else:
                table.append(main_table[table_count])
                text(table[0][0], (15, 140), 20)
                text(table[0][1], (15, 170), 20)
                text(table[0][2], (15, 200), 20)
                text(table[0][3], (15, 230), 20)
                screen.blit(next_button, (250, 150))
                if mouse[0] in (250, 300) and mouse[1] in (150, 200):
                    game_state = 'Replay'
                    filename = str(table[0][4])
                    with open(filename, 'r') as file:
                        fr = csv.reader(file)
                        for rec in fr:
                            replay_list.append(rec)
                text(str(table[0][5]), (480, 170), 20)
                table=[]
        else:
            text('Your Play has been recorded', (100, 20), 30)
            text('Do you want to watch the replay', (10, 180), 40)
            screen.blit(next_button, (300, 250))
            if mouse[0] in (300, 350) and mouse[1] in (250, 300):
                game_state = 'Replay'
                filename = '{}.csv'.format(fname)
    if game_state=='Replay':
        screen.fill(colour)
        screen.blit(BoardImg, (250, 50))
        screen.blit(TitleImg, (25, 50))
        screen.blit(redplayerImg, red_path[red_1])
        screen.blit(redplayerImg, red_path[red_2])
        screen.blit(redplayerImg, red_path[red_3])
        screen.blit(redplayerImg, red_path[red_4])
        screen.blit(greenplayerImg, green_path[green_1])
        screen.blit(greenplayerImg, green_path[green_2])
        screen.blit(greenplayerImg, green_path[green_3])
        screen.blit(greenplayerImg, green_path[green_4])
        screen.blit(blueplayerImg, blue_path[blue_1])
        screen.blit(blueplayerImg, blue_path[blue_2])
        screen.blit(blueplayerImg, blue_path[blue_3])
        screen.blit(blueplayerImg, blue_path[blue_4])
        screen.blit(yellowplayerImg, yellow_path[yellow_1])
        screen.blit(yellowplayerImg, yellow_path[yellow_2])
        screen.blit(yellowplayerImg, yellow_path[yellow_3])
        screen.blit(yellowplayerImg, yellow_path[yellow_4])
        screen.blit(next_button, (580, 0))
        text(tbd, (250, 10), 32, text_colour)
        tbd=str(dice_output)
        if last_played!=None:
            text(str(Players[Chance]) +' PLAYING', (10, 150), 28, text_colour)
        text("Red", (10, 410), 25, text_colour)
        text("Yellow", (10, 460), 25, text_colour)
        text("Green", (325, 410), 25, text_colour)
        text("Blue", (325, 460), 25, text_colour)
        if dice_state == "ready" or dice_state == "value":
            colour = colours[Chance]
            text_colour = text_colours[Chance]
        else:
            colour = (255, 235, 205)
            text_colour = (0, 0, 0)
        if dice_state == "value":
            if dice_type == 'dice':
                dice()
            else:
                kavade()
        left, middle, right = pygame.mouse.get_pressed(3)
        if left:
            mouse = pygame.mouse.get_pos()
            mx, my = mouse
            mx, my = (mx // 50) * 50, (my // 50) * 50
            mouse = (mx, my)
        else:
            mouse = (0, 0)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    time.sleep(0.1)
                    replay_count+=2
                    all = replay_list[replay_count]
                    if len(replay_list) != replay_count + 1:
                        other_info = replay_list[replay_count + 1]
                    print(all)
        if (mouse[0] >= 580 and mouse[1] <= 50):
            time.sleep(0.1)
            replay_count += 2
            all = replay_list[replay_count]
            print(all)
            print(len(replay_list),replay_count)
            if len(replay_list)!=replay_count +1:
                other_info = replay_list[replay_count + 1]
        if all[1]=='Eof':
            winner=all[0]
            game_state='Winner'
            replay_count=0
            replay_list=[]
        if game_state!='Winner':
            for i in range(16):
                all[i] = int(all[i])
            [red_1, yellow_1, green_1, blue_1, red_2, yellow_2, green_2, blue_2, red_3, yellow_3, green_3, blue_3, red_4,yellow_4, green_4, blue_4] = all
            last_played = other_info[0]
            dice_output = int(other_info[1])
            Chance = int(other_info[2])
            dice_state = other_info[3]
            dice_type = other_info[4]
    try:
        pygame.display.update()
    except:
        continue
if insert_count == 0:
    os.remove('{}.csv'.format(fname))
    print('file deleted')
co.close()
