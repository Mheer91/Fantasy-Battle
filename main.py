import pygame
import os
import random
import time


pygame.font.init()

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fantasy Battle")

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()


    # def redraw_window():
    #     WIN.blit((0,0))

    while run:
        clock.tick(FPS)
        # redraw_window()

main()