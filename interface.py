import pygame
import os
from y import one as coder
from y import two as decoder

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Window
pygame.display.set_caption("escape_from_vet")  # Project Name
FPS = 60  # Max FPS
INTRO = pygame.image.load(os.path.join('kartinki', 'intro.png'))
INTRO = pygame.transform.smoothscale(INTRO, (WIDTH, HEIGHT))


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
    print(coder('q'))
    print(decoder('623G14Z'))
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():  # Checking for keys pressed / game closed
            if event.type == pygame.QUIT:  # Game is closed
                run = False
            if event.type == pygame.KEYDOWN:
                if mode == 0:
                    mode = 1
                elif mode == 1:
                    if event.key == pygame.K_UP:
                        n -= 1
                    elif event.key == pygame.K_DOWN:
                        n += 1
                    elif event.key == pygame.K_RETURN:
                        mode = 2
                elif mode == 2:
                    if event.key == pygame.K_RETURN:
                        mode = 3
        if mode == 0:
            draw_intro()
        elif mode == 1:
            draw_pick_side(n % 2)
        elif mode == 2:
            draw_info(n)
        elif mode == 3:
            draw_room(n)


if __name__ == '__main__':
    main()
