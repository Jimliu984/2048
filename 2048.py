import pygame
import numpy as np
import sys
import random
pygame.init()
pygame.display.set_caption('2048')
WIDTH = 800
HEIGHT = 800
Dim = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((185, 173, 161))
### Game in array
Game = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
pygame.font.init()
default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 80)
#Colours = [(236, 228, 220),(231, 131, 103),(223, 145, 96),(232, 180, 129),(235, 223, 203),(232, 180, 129),\
#           (229, 194, 83),(237, 209, 99),(240, 179, 124),(235, 223, 203),(129, 214, 154)] #2048
Colours = [(255,229,204),(255,204,153),(255,175,102),(250,132,132),(255,81,81),(255,30,30),(255,255,102),\
           (250,230,90),(250,220,50),(250,220,0),(100,250,0),(50,250,0),(0,200,0),(0,0,250),(0,0,200),(0,0,100)]
def Create_New_Tiles(Game):
    List = []
    for y in range(4):
        for x in range(4):
            if Game[y][x] == 0:
                List.append(4*y+x)
    Value = random.choice(List)
    a = int(Value%4)
    b = int((Value-a)/4)
    Game[b][a]=random.randrange(2,5,2)
Create_New_Tiles(Game)
Create_New_Tiles(Game)
def Move_Left(Game):
    Game_Copy = Game.copy()
    for a in range(4):
        Row = Game[a]
        for b in range(4):
            for c in range(b+1,4):
                if Row[b] == 0 and Row[c]!=0:
                        Row[b] = Row[c]
                        Row[c] = 0
        for x in range(3):
            if Row[x]==Row[x+1]:
                Row[x] = Row[x]*2
                Row[x+1] = 0
            elif Row[x]==0:
                Row[x] = Row[x+1]
                Row[x + 1] = 0
    if np.array_equal(Game_Copy,Game) == False:
        Create_New_Tiles(Game)
def Move_Right(Game):
    Game_Copy = Game.copy()
    for a in range(4):
        Row = Game[a][::-1]
        for b in range(4):
            for c in range(b+1,4):
                if Row[b] == 0 and Row[c]!=0:
                        Row[b] = Row[c]
                        Row[c] = 0
        for x in range(3):
            if Row[x] == Row[x + 1]:
                Row[x] = Row[x] * 2
                Row[x + 1] = 0
            elif Row[x] == 0:
                Row[x] = Row[x + 1]
                Row[x + 1] = 0
    if np.array_equal(Game_Copy, Game) == False:
        Create_New_Tiles(Game)
def Move_Up(Game):
    Game_Copy = Game.copy()
    for a in range(4):
        Col = Game[:,a]
        for b in range(4):
            for c in range(b+1,4):
                if Col[b] == 0 and Col[c]!=0:
                        Col[b] = Col[c]
                        Col[c] = 0
        for x in range(3):
            if Col[x] == Col[x + 1]:
                Col[x] = Col[x] * 2
                Col[x + 1] = 0
            elif Col[x] == 0:
                Col[x] = Col[x + 1]
                Col[x + 1] = 0
    if np.array_equal(Game_Copy, Game) == False:
        Create_New_Tiles(Game)
def Move_Down(Game):
    Game_Copy = Game.copy()
    for a in range(4):
        Col = Game[:,a][::-1]
        for b in range(4):
            for c in range(b+1,4):
                if Col[b] == 0 and Col[c]!=0:
                        Col[b] = Col[c]
                        Col[c] = 0
        for x in range(3):
            if Col[x] == Col[x + 1]:
                Col[x] = Col[x] * 2
                Col[x + 1] = 0
            elif Col[x] == 0:
                Col[x] = Col[x + 1]
                Col[x + 1] = 0
    if np.array_equal(Game_Copy, Game) == False:
        Create_New_Tiles(Game)
def Check_Game(Game):
    if 2048 in Game:
        print("Win")
    Lose = 0
    for a in range(3):
        for b in range(3):
            if (0 not in Game) and Game[a,b]!=Game[a+1,b] and Game[a,b]!=Game[a,b+1] and Game[3,b]!=Game[3,b+1] and Game[a,3]!=Game[a+1,3]:
                Lose += 1
    if Lose == 9:
        label = font_renderer.render("Game Over", 1, (0, 0, 0))
        label_rect = label.get_rect(center=(400,400))
        screen.blit(label, label_rect)
def Draw_Game(Game):
    for a in range(4):
        for b in range(4):
            if Game[a, b] == 0:
                pygame.draw.rect(screen, (255, 255, 255), (b * Dim+5, a * Dim+5, Dim-10, Dim-10))
            else:
                pygame.draw.rect(screen, Colours[int(np.log2(Game[a, b])-1)], (b * Dim+5, a * Dim+5, Dim-10, Dim-10))
                label = font_renderer.render(str(Game[a, b]), 1, (0, 0, 0))
                label_rect = label.get_rect(center=(b*Dim+100,a*Dim+100))
                screen.blit(label, label_rect)
Draw_Game(Game)
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Move_Left(Game)
            elif event.key == pygame.K_RIGHT:
                Move_Right(Game)
            elif event.key == pygame.K_UP:
                Move_Up(Game)
            elif event.key == pygame.K_DOWN:
                Move_Down(Game)
            Draw_Game(Game)
            Check_Game(Game)
    pygame.display.update()
