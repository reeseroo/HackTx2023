from Users import mongoDB
from functions import Active
from functions import Passive
import pygame
import pygame_widgets
from pygame_widgets.button import Button


def home_screen(display, clock, user):
    #to-do
    mongoDB.characterFind(user)
    print("todo")
    activeButton = Button(
        display,
        40,
        480,
        300,
        100,

        text  = "Active",
        fontSize=50,
        margin=20,
        inactiveColour=(191, 143, 101),
        hoverColour=(236, 197, 163),
        pressedColour=(233, 137, 53),
        radius=20,
        onClick=lambda: Passive.passive_screen(display, clock)
    )

    passiveButton = Button(
        display,
        480,
        480,
        300,
        100,

        text  = "Active",
        fontSize=50,
        margin=20,
        inactiveColour=(191, 143, 101),
        hoverColour=(236, 197, 163),
        pressedColour=(233, 137, 53),
        radius=20,
        onClick=lambda: Passive.passive_screen(display, clock)
    )
    dis = (218, 108, 177)
    bN = (191, 143, 101)
    bL = (236, 197, 163)
    width = display.get_width()
    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        display.fill((218, 108, 177))

        pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
        pygame.display.update()
    #Display Character
    #Display Passive Button
    #Display Active Button
    #Display LeaderBoard