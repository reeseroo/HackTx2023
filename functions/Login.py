import pygame


def login_screen(display, clock):
    # Font and Colors
    color = (255, 255, 255)
    font = 'Black'
    smallfont = pygame.font.SysFont(font, 32)

    # Text Coordinates
    width = display.get_width()
    height = display.get_height()
    instruction_coords = [(width / 2 - 250, height / 2 - 150), (width / 2 - 250, height / 2 - 100)]
    prompt_coords = (width / 2 - 200, height / 2)

    background = pygame.image.load('sprites/background.jpg')

    # Start screen
    while True:
        display.fill((0, 0, 0))
        display.blit(background, [0, 0])
        pygame.display.set_caption("Gamify | Help youself")

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 0
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)
        pygame.display.update()