import os
import sys
import traceback
import pygame
import numpy as np
class Initiate(object):
    background_color=(200,200,200)
    show_color=(18,118,38)
    os.chdir(sys.path[0])
    Black_chess=os.path.abspath('Black_chess.png') 
    White_chess=os.path.abspath('White_chess.png')

    def __init__(self,screen,x,y,color,map):
        self.screen=screen
        self.map=map

    def draw_chessboard(self):
        self.screen.fill(self.background_color)
        for i in range(1,20):
            pygame.draw.line(self.screen,self.show_color,(40*i+5,45),(40*i+5,40*19+5))
            pygame.draw.line(self.screen,self.show_color,(45,40*i+5),(40*19+5,40*i+5))
        pygame.display.flip()

    def draw_chessman(self):
        if self.color==0:
            black=pygame.image.load(self.Black_chess)
            self.screen.blit(black,(40*self.x+5-0.5*35,40*self.y+5-0.5*35))
            print("0")
        elif self.color==1:
            white=pygame.image.load(self.White_chess)
            self.screen.blit(white,(40*self.x+5-0.5*35,40*self.y+5-0.5*35))
            print("1")
        pygame.display.flip()
    
    def winner(self):
        delta=0
        for i in range(5):
            if (self.map[self.x-i][self.y]==self.map[self.x-i+1][self.y]==self.map[self.x-i+2][self.y]==self.map[self.x-i+3][self.y]==self.map[self.x-i+4][self.y]==color):
                delta=1
            if (self.map[self.x][self.y-i]==self.map[self.x][self.y-i+1]==self.map[self.x][self.y-i+2]==self.map[self.x][self.y-i+3]==self.map[self.x][self.y-i+4]==color):
                delta=1
            if (self.map[self.x-i][self.y-i]==self.map[self.x-i+1][self.y-i+1]==self.map[self.x-i+2][self.y-i+2]==self.map[self.x-i+3][self.y-i+3]==self.map[self.x-i+4][self.y-i+4]==color):
                delta=1
            if (self.map[self.x-i][self.y+i]==self.map[self.x-i+1][self.y+i-1]==self.map[self.x-i+2][self.y+i-2]==self.map[self.x-i+3][self.y+i-3]==self.map[self.x-i+4][self.y+i-4]==color): 
                delta=1
        return delta

    def print_text(self,text,size):                   #提示文字
        text_font=pygame.font.SysFont("Comic Sans MS",size)
        text_show=text_font.render(text,True,self.show_color)
        self.screen.blit(text_show,(self.x,self.y))
        pygame.display.flip()
        print(text)
