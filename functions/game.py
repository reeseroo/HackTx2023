import pygame
from functions import Login, Home, Passive, Active



def start_game():
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode()
    Login.Login_screen(display, clock)