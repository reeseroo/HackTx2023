import pygame
import pygame_widgets
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
import sys
from Users import mongoDB
from functions import Home


def login_screen(display, clock):
    def output():
        username = user.getText()
        password2 = password.getText()
        if mongoDB.userFind(username, password2) == 1:
            Home.home_screen(display, clock, username)


    display = pygame.display.set_mode((1000, 600))

    user = TextBox(display, 100, 100, 800, 80, fontSize=50,
                      borderColour=(0, 0, 0), textColour=(0, 0, 0),radius=10, borderThickness=5)
    password = TextBox(display, 100, 300, 800, 80, fontSize=50,
                   borderColour=(0, 0, 0), textColour=(0, 0, 0), radius=10, borderThickness=5)
    button = Button(
        # Mandatory Parameters
        display,  # Surface to place button on
        300,  # X-coordinate of top left corner
        450,  # Y-coordinate of top left corner
        300,  # Width
        150,  # Height

        # Optional Parameters
        text='Login',  # Text to display
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=output  # Function to call when clicked on
    )
    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        display.fill((255, 255, 255))

        pygame_widgets.update(events)
        pygame.display.update()

    '''
   if mongoDB.userFind("Jenna", "2345") == 1:
        print("true")

    while True:
        display.fill((0, 0, 0))
        pygame.display.set_caption("Login Screen")

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 0
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)
        pygame.display.update()
        '''
