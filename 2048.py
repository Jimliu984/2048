import pygame
import numpy as np
import sys
import random

pygame.init()
pygame.display.set_caption('2048')
WIDTH = 720
HEIGHT = 720
Dim = 180
screen = pygame.display.set_mode((WIDTH, HEIGHT + 80))
### Game in array
pygame.font.init()
default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 80)
font_renderer2 = pygame.font.Font(default_font, 35)
# Colours of Tiles
Colours = [(255, 229, 204), (255, 204, 153), (255, 175, 102), (250, 132, 132), (255, 81, 81), (255, 30, 30),
           (255, 255, 102),
           (250, 230, 90), (250, 220, 50), (250, 220, 0), (100, 250, 0), (50, 250, 0), (0, 200, 0), (0, 0, 250),
           (0, 0, 200), (0, 0, 100)]
WHITE = pygame.Color(255, 255, 255)


def create_new_tiles(game):
    List = []
    for y in range(4):
        for x in range(4):
            if game[y][x] == 0:
                List.append(4 * y + x)
    Value = random.choice(List)
    a = int(Value % 4)
    b = int((Value - a) / 4)
    game[b][a] = random.randrange(2, 5, 2)


def move_left(game):
    game_copy = game.copy()
    for a in range(4):
        row = game[a]
        for b in range(4):
            for c in range(b + 1, 4):
                if row[b] == 0 and row[c] != 0:
                    row[b] = row[c]
                    row[c] = 0
        for x in range(3):
            if row[x] == row[x + 1]:
                row[x] = row[x] * 2
                row[x + 1] = 0
            elif row[x] == 0:
                row[x] = row[x + 1]
                row[x + 1] = 0
    if np.array_equal(game_copy, game) == False:
        create_new_tiles(game)


def move_right(game):
    game_copy = game.copy()
    for a in range(4):
        row = game[a][::-1]
        for b in range(4):
            for c in range(b + 1, 4):
                if row[b] == 0 and row[c] != 0:
                    row[b] = row[c]
                    row[c] = 0
        for x in range(3):
            if row[x] == row[x + 1]:
                row[x] = row[x] * 2
                row[x + 1] = 0
            elif row[x] == 0:
                row[x] = row[x + 1]
                row[x + 1] = 0
    if np.array_equal(game_copy, game) == False:
        create_new_tiles(game)


def move_up(game):
    game_copy = game.copy()
    for a in range(4):
        Col = game[:, a]
        for b in range(4):
            for c in range(b + 1, 4):
                if Col[b] == 0 and Col[c] != 0:
                    Col[b] = Col[c]
                    Col[c] = 0
        for x in range(3):
            if Col[x] == Col[x + 1]:
                Col[x] = Col[x] * 2
                Col[x + 1] = 0
            elif Col[x] == 0:
                Col[x] = Col[x + 1]
                Col[x + 1] = 0
    if np.array_equal(game_copy, game) == False:
        create_new_tiles(game)


def move_down(game):
    game_copy = game.copy()
    for a in range(4):
        col = game[:, a][::-1]
        for b in range(4):
            for c in range(b + 1, 4):
                if col[b] == 0 and col[c] != 0:
                    col[b] = col[c]
                    col[c] = 0
        for x in range(3):
            if col[x] == col[x + 1]:
                col[x] = col[x] * 2
                col[x + 1] = 0
            elif col[x] == 0:
                col[x] = col[x + 1]
                col[x + 1] = 0
    if np.array_equal(game_copy, game) == False:
        create_new_tiles(game)


def check_game(game):
    if 2048 in game:
        label = font_renderer2.render("You did it!", True, (0, 0, 0))
        screen.blit(label, (100, 720))
        label = font_renderer2.render("Keep Going!", True, (0, 0, 0))
        screen.blit(label, (100, 760))
    lose = 0
    for a in range(3):
        for b in range(3):
            if (0 not in game) and game[a, b] != game[a + 1, b] and game[a, b] != game[a, b + 1] and game[3, b] != game[
                3, b + 1] and game[a, 3] != game[a + 1, 3]:
                lose += 1
    if lose == 9:
        label = font_renderer2.render("Game Over!", True, (0, 0, 0))
        screen.blit(label, (100, 720))
        label = font_renderer2.render("Press Space to Restart", True, (0, 0, 0))
        screen.blit(label, (100, 760))


def draw_game(game):
    shift = 5
    rect_size = Dim - 10
    for a in range(4):
        for b in range(4):
            if game[a, b] == 0:
                pygame.draw.rect(screen, WHITE, (b * Dim + shift, a * Dim + shift, rect_size, rect_size))
            else:
                pygame.draw.rect(screen, Colours[int(np.log2(game[a, b]) - 1)],
                                 (b * Dim + 5, a * Dim + 5, Dim - 10, Dim - 10))
                label = font_renderer.render(str(game[a, b]), True, (0, 0, 0))
                label_rect = label.get_rect(center=(b * Dim + shift + rect_size / 2, a * Dim + shift + rect_size / 2))
                screen.blit(label, label_rect)


def play_game():
    screen.fill((185, 173, 161))
    game = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    create_new_tiles(game)
    create_new_tiles(game)
    draw_game(game)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play_game()
                if event.key == pygame.K_LEFT:
                    move_left(game)
                elif event.key == pygame.K_RIGHT:
                    move_right(game)
                elif event.key == pygame.K_UP:
                    move_up(game)
                elif event.key == pygame.K_DOWN:
                    move_down(game)
                draw_game(game)
                check_game(game)
        pygame.display.update()


play_game()
