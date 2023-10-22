import pygame
import pygame_widgets
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
import sys
from Users import mongoDB
from functions import Home, button


def login_screen(display, clock, user2):
    def output():
        username = user.getText()
        password2 = password.getText()
        if mongoDB.userFind(username, password2) == 1:
            print(username)
            user2.set_userID(username)
            #Home.home_screen(display, clock, user2)
            return 1
        else:
            return 0
    
    
   # display = pygame.display.set_mode()
    screen_width, screen_height = display.get_size() 
    login_img = pygame.image.load('sprites/login_button.jpg')
    register_img = pygame.image.load('sprites/register_button.jpg')
    login_button = button.Button(screen_width*0.5, screen_height*0.5, login_img, 0.8)
    register_button = button.Button(screen_width*0.2, screen_height*0.5, register_img, 0.8)

    user = TextBox(display, 100, 100, 400, 80, fontSize=25,
                      borderColour=(0, 0, 0), textColour=(0, 0, 0),radius=10, borderThickness=5)
    password = TextBox(display, 100, 300, 400, 80, fontSize=25,
                   borderColour=(0, 0, 0), textColour=(0, 0, 0), radius=10, borderThickness=5)

    


    run = True
    
    display.fill((234, 212, 252))
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()
            # Check for QUIT event	 
            if event.type == pygame.QUIT: 
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
                                   
        register_button.draw(display)
        if login_button.draw(display):
            if output()==1:
                Home.home_screen(display, clock, user2)
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
