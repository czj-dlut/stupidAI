import numpy as np
import pygame
import os
import sys
import traceback
import copy
from pygame.locals import *
from min_max_search import *


os.chdir(sys.path[0])
Black_chess=os.path.abspath('Black_chess.png')  
White_chess=os.path.abspath('White_chess.png')

pygame.init()
pygame.mixer.init()

background_color=(200,200,200)
show_color=(18,118,38)

def draw_chessboard(screen):
    screen.fill(background_color)
    for i in range(1,20):
        pygame.draw.line(screen,show_color,(40*i+5,45),(40*i+5,40*19+5))
        pygame.draw.line(screen,show_color,(45,40*i+5),(40*19+5,40*i+5))
    pygame.display.flip()

def draw_chessman(x,y,screen,color):
    if color==0:
        black=pygame.image.load(Black_chess)
        screen.blit(black,(40*x+5-0.5*35,40*y+5-0.5*35))
        print("0")
    elif color==1:
        white=pygame.image.load(White_chess)
        screen.blit(white,(40*x+5-0.5*35,40*y+5-0.5*35))
        print("1")
    pygame.display.flip()

def winner(x,y,color):
    delta=0
    for i in range(5):
        if (map[x-i][y]==map[x-i+1][y]==map[x-i+2][y]==map[x-i+3][y]==map[x-i+4][y]==color):
            delta=1
        if (map[x][y-i]==map[x][y-i+1]==map[x][y-i+2]==map[x][y-i+3]==map[x][y-i+4]==color):
            delta=1
        if (map[x-i][y-i]==map[x-i+1][y-i+1]==map[x-i+2][y-i+2]==map[x-i+3][y-i+3]==map[x-i+4][y-i+4]==color):
            delta=1
        if (map[x-i][y+i]==map[x-i+1][y+i-1]==map[x-i+2][y+i-2]==map[x-i+3][y+i-3]==map[x-i+4][y+i-4]==color): 
            delta=1
    return delta


def print_text(text,screen,size,x,y):                   #提示文字
    text_font=pygame.font.SysFont("Comic Sans MS",size)
    text_show=text_font.render(text,True,show_color)
    screen.blit(text_show,(x,y))
    pygame.display.flip()
    print(text)

def initiate(screen):
    global map,color
    color=0
    map=[[-1 for col in range(25)] for row in range(25)]
    draw_chessboard(screen)
    print_text("replay",screen,30,830,560)
    print_text("exit",screen,30,830,660)
    print_text("AI run?",screen,30,830,460)

def main():
    global map,color
    screen = pygame.display.set_mode([1000,785])
    AI=False
    initiate(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y =event.pos[0],event.pos[1]
                    if (800<x<950) and (550<y<640):
                        initiate(screen)
                        continue
                    elif (800<x<950) and (650<y<740):
                        pygame.quit()
                        sys.exit()
                    elif (800<x<950) and (450<y<540):
                        AI=(not (AI))
                    else:
                        for i in range(1,20):
                            for j in range(1,20):
                                if ((i-1)*40+35<x<(i-1)*40+55) and ((j-1)*40+35<y<(j-1)*40+55) and (map[i][j]==-1):
                                    draw_chessman(i,j,screen,color)
                                    map[i][j]=color 
                                    color=not(color)
                                    if (winner(i,j,not(color))):
                                        if AI:
                                            print_text("human win!",screen,45,775,200)
                                        elif color:
                                            print_text("black win!",screen,45,775,200)
                                        else:
                                            print_text("white win!",screen,45,775,200)
                                        map=[[1 for col in range(25)] for row in range(25)]
                                    elif AI:
                                        (a,b)=AI_search(map)
                                        map[a][b]=color
                                        draw_chessman(a,b,screen,color)
                                        color=not(color)
                                        if (winner(a,b,not(color))):
                                            print_text("AI win!",screen,45,775,200)
                                            map=[[1 for col in range(25)] for row in range(25)]
                                        

if __name__ == "__main__":
    main()    
                    


        

        