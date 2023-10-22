import pygame
from functions import Login, Home, Passive, Active



def start_game():
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode()
    #Login.login_screen(display, clock)
    Passive.passive_screen(display, clock)