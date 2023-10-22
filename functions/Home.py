from pygame import font
import sys
from Users import mongoDB
from functions import Active
from functions import Passive
import pygame
import pygame_widgets
from pygame_widgets.button import Button


def home_screen(display, clock, user):
    display.fill((218, 108, 177))
    pygame.display.update()

    user.set_char(mongoDB.characterFind(user.get_userID()))
    user.set_health(mongoDB.getCharacterHealth(user.get_userID(), user.get_char()))
    user.set_wealth(mongoDB.getCharacterWealth(user.get_userID(), user.get_char()))
    activeButton = Button(
        display,
        40,
        480,
        300,
        100,

        text="Active",
        fontSize=50,
        margin=20,
        inactiveColour=(191, 143, 101),
        hoverColour=(236, 197, 163),
        pressedColour=(233, 137, 53),
        radius=20,
        onClick=lambda: Active.active_screen(display, clock)
    )

    passiveButton = Button(
        display,
        480,
        480,
        300,
        100,

        text="Passive",
        fontSize=50,
        margin=20,
        inactiveColour=(191, 143, 101),
        hoverColour=(236, 197, 163),
        pressedColour=(233, 137, 53),
        radius=20,
        onClick=lambda: Passive.passive_screen(display, clock, user)
    )
    dis = (218, 108, 177)
    bN = (191, 143, 101)
    bL = (236, 197, 163)
    width = display.get_width()
    height = display.get_height()
    font = pygame.font.Font(None, 36)
    money = user.get_wealth()
    money_text = font.render(f"Money: {money}", True, (255, 255, 255))
    money_coords = (width - money_text.get_width() - 20, 20)
    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()

        display.fill((218, 108, 177))
        # Blit the money text on the display
        display.blit(money_text, money_coords)
        pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen

        pygame.display.update()
    # Display Character
    avatar = mongoDB.characterFind(user)
    # health = mongoDB.healthFind(user) #getting the health of the character for future displaying
    # wealth = mongoDB.wealthFind(user) #for getting the wealth of the character for future displaying

    # Display LeaderBoard

    #health = mongoDB.healthFind(user) #getting the health of the character for future displaying
    #wealth = mongoDB.wealthFind(user) #for getting the wealth of the character for future displaying
    
    #Display LeaderBoard