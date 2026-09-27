from settings import *

class Button:
    def __init__(self, text, color, x, y, font):
        self.x = x
        self.y = y
        self.font = font
        self.text = text
        self.color = color
        self.size = BUTTON_SIZE
        self.hitbox = pygame.Rect(x, y, self.size[0], self.size[1])

    def draw(self, screen):
        text_image = self.font.render(self.text, True, TEXT_COLOR)
        pygame.draw.rect(screen, self.color, self.hitbox, border_radius = 30)

        screen.blit(text_image, (self.x + TEXT_PADDING_H,
                                 self.y + TEXT_PADDING_V))