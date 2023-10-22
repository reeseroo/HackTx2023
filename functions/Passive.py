# import the pygame module 
import pygame, sys
from functions import button



def passive_screen(display, clock):

	start_img = pygame.image.load('sprites/start_btn.png')
	exit_img = pygame.image.load('sprites/exit_btn.png')
	start_button = button.Button(100, 200, start_img, 0.8)
	exit_button = button.Button(450, 200, exit_img, 0.8)

	width, height = display.get_size()

	# Define the background colour 
	# using RGB color coding. 
	background_colour = (234, 212, 252) 
	display.fill(background_colour)
	pygame.display.flip()
	x = 100
	y = 100

	
	# Variable to keep our game loop running 
	running = True
	# game loop 
	while running: 

		if start_button.draw(display):
			print('START')
		if exit_button.draw(display):
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
		pygame.display.flip()
