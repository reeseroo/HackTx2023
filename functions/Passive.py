# import the pygame module 
import pygame, sys
from functions import button, Home

def passive_screen(display, clock, user):


	screen_width, screen_height = display.get_size() 

	home_img = pygame.image.load('sprites/home_button.jpg')
	active_img = pygame.image.load('sprites/active_button.jpg')
	home_button = button.Button(screen_width*0.03, screen_height*0.05, home_img, 0.8)
	active_button = button.Button(screen_width * 0.7, screen_height*.05, active_img, 0.8)

	# Define the background colour 
	# using RGB color coding. 
	background_colour = (234, 212, 252) 
	display.fill(background_colour)
	pygame.display.flip()
	
	# Variable to keep our game loop running 
	running = True
	# game loop 
	while running: 

		if home_button.draw(display): #if the button is clicked
			Home.home_screen(display, clock, user)
		if active_button.draw(display):
			print('EXIT')
	
	# for loop through the event queue 
		for event in pygame.event.get(): 
	
			# Check for QUIT event	 
			if event.type == pygame.QUIT: 
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
					pygame.quit()
					sys.exit()
			
        #refresh
		pygame.display.update()

