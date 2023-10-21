import pygame
import sys
from Users import mongoDB


def login_screen(display, clock):
    background = pygame.image.load('sprites/background.jpg')
    if mongoDB.userFind("Jenna", "2345") == 1:
        print("true")

    mongoDB.addNewUser()
    while True:
        display.fill((0, 0, 0))
        display.blit(background, [0, 0])
        pygame.display.set_caption("Login Screen")

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 0
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)
        pygame.display.update()
