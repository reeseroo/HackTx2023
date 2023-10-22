import pygame
from functions import Login, Home, Passive, Active, player



def start_game():
    user = player.player()
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode()
    Login.login_screen(display, clock, user)
    #Passive.passive_screen(display, clock, user)