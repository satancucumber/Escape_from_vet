import pygame
import os
from random import randrange
from algorithms import coder
from algorithms import decoder

pygame.init()
font = pygame.font.Font(os.path.join('Fonts', 'Inconsolata-VariableFont_wdth,wght.ttf'), 18)
font2 = pygame.font.Font(os.path.join('Fonts', 'Inconsolata-VariableFont_wdth,wght.ttf'), 8)
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Window
pygame.display.set_caption("Побег от ветеринара")  # Project Name
FPS = 60  # Max FPS
INTRO = pygame.image.load(os.path.join('kartinki', 'intro.png'))
INTRO = pygame.transform.smoothscale(INTRO, (WIDTH, HEIGHT))

passwords = ["320GB4Z31223B4Z421G44Z", "421G64Z2122314Z421G44Z", "220G14Z235974Z220G34Z"]
keywords = ["KOT", "VET", "ABC"]

def draw_win(n):
    picker = pygame.image.load(os.path.join('kartinki', 'win' + str(n % 2) + '.png'))
    picker = pygame.transform.smoothscale(picker, (WIDTH, HEIGHT))
    WIN.blit(picker, (0, 0))
    pygame.display.update()

def draw_game_over(n):
    picker = pygame.image.load(os.path.join('kartinki', 'gameover' + str(n % 2) + '.png'))
    picker = pygame.transform.smoothscale(picker, (WIDTH, HEIGHT))
    WIN.blit(picker, (0, 0))
    pygame.display.update()

def checking1(text, pass_text):
    if text == decoder(pass_text):
        return True
    return False

def checking0(text, key_text):
    if text == coder(key_text):
        return True
    return False

def draw_scrin1(text, pass_text, attempt):
    picker = pygame.image.load(os.path.join('kartinki', 'scrin1' + str(attempt) + '.png'))
    picker = pygame.transform.smoothscale(picker, (WIDTH, HEIGHT))
    WIN.blit(picker, (0, 0))
    heart = pygame.image.load(os.path.join('kartinki', 'heart' + str(attempt) + '.png'))
    WIN.blit(heart, (1109, 90))
    press_surface = font.render(pass_text, True, (0, 0, 0))
    key_surface = font.render(text, True, (0, 0, 0))
    WIN.blit(press_surface, (765, 305))
    WIN.blit(key_surface, (990, 520))
    pygame.display.update()

def draw_scrin0(text, key_text, attempt):
    picker = pygame.image.load(os.path.join('kartinki', 'scrin0' + str(attempt) + '.png'))
    picker = pygame.transform.smoothscale(picker, (WIDTH, HEIGHT))
    WIN.blit(picker, (0, 0))
    heart = pygame.image.load(os.path.join('kartinki', 'heart' + str(attempt) + '.png'))
    WIN.blit(heart, (1109, 90))
    press_surface = font.render(text, True, (0, 0, 0))
    key_surface = font.render(key_text, True, (0, 0, 0))
    WIN.blit(press_surface, (765, 303))
    WIN.blit(key_surface, (990, 512))
    pygame.display.update()

def draw_room(n):
    picker = pygame.image.load(os.path.join('kartinki', 'gp' + str(n % 2) + 'room' + '.png'))
    picker = pygame.transform.smoothscale(picker, (WIDTH, HEIGHT))
    WIN.blit(picker, (0, 0))
    pygame.display.update()


def draw_info(n):
    picker = pygame.image.load(os.path.join('kartinki', 'gp' + str(n % 2) + 'info' + '.png'))
    picker = pygame.transform.smoothscale(picker, (WIDTH, HEIGHT))
    WIN.blit(picker, (0, 0))
    pygame.display.update()


def draw_pick_side(n):
    picker = pygame.image.load(os.path.join('kartinki', 'menu' + str(n) + '.png'))
    picker = pygame.transform.smoothscale(picker, (WIDTH, HEIGHT))
    WIN.blit(picker, (0, 0))
    pygame.display.update()


def draw_intro():
    WIN.blit(INTRO, (0, 0))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    mode = 0
    n = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():  # Checking for keys pressed / game closed
            if event.type == pygame.QUIT:  # Game is closed
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if mode == 0:
                    mode = 1
                elif mode == 1:
                    if event.key == pygame.K_UP:
                        n -= 1
                    elif event.key == pygame.K_DOWN:
                        n += 1
                    elif event.key == pygame.K_RETURN:
                        pass_text = passwords[randrange(0, 3)]
                        key_text = keywords[randrange(0, 3)]
                        text = ''
                        attempt = 0
                        mode = 2
                elif mode == 2:
                    if event.key == pygame.K_RETURN:
                        mode = 3
                elif mode == 3:
                    if event.key == pygame.K_RETURN:
                        mode = 4
                elif mode == 4 and n % 2 == 0:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[0:len(text)-1:1]
                    elif event.key == pygame.K_RETURN:
                        if checking0(text, key_text):
                            mode = 6
                        elif attempt == 2:
                            mode = 5
                        else:
                            attempt += 1
                        text = ''
                    else:
                        text += event.unicode
                elif mode == 4 and n % 2 == 1:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[0:len(text)-1:1]
                    elif event.key == pygame.K_RETURN:
                        if checking1(text, pass_text):
                            mode = 6
                        elif attempt == 2:
                            mode = 5
                        else:
                            attempt += 1
                        text = ''
                    else:
                        text += event.unicode
                elif mode == 5 or mode == 6:
                    if event.key == pygame.K_RETURN:
                        mode = 1


        if mode == 0:
            draw_intro()
        elif mode == 1:
            draw_pick_side(n % 2)
        elif mode == 2:
            draw_info(n)
        elif mode == 3:
            draw_room(n)
        elif mode == 4 and n % 2 == 0:
            draw_scrin0(text, key_text, attempt)
        elif mode == 4 and n % 2 == 1:
            draw_scrin1(text, pass_text, attempt)
        elif mode == 5:
            draw_game_over(n)
        elif mode == 6:
            draw_win(n)
if __name__ == '__main__':
    main()