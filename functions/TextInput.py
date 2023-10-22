import pygame


class TextInput(pygame.sprite.Sprite):
    def __init__(self, x, y, width=100, height=50, color=(0, 0, 0),
                 bgcolor=(0, 255, 0), selectedColor=(0, 0, 255)):
        super().__init__()
        self.text_value = ""
        self.isSelected = False
        self.color = color
        self.bgcolor = bgcolor
        self.selectedColor = selectedColor

        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(self.text_value, True, self.color)
        self.bg = pygame.Rect(x, y, width, height)