import pygame
from functions import Login, Home, Passive, Active



def start_game():
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((800, 600))
    Login.login_screen(display, clock)