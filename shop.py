import sys

from settings import *
from button import Button

bg1_image = pygame.transform.scale(pygame.image.load('backgrounds/bg1.jpg'),
                                   (SCREEN_WIDTH, SCREEN_HEIGHT))
bg2_image = pygame.transform.scale(pygame.image.load('backgrounds/bg2.jpg'),
                                   (SCREEN_WIDTH, SCREEN_HEIGHT))
bg3_image = pygame.transform.scale(pygame.image.load('backgrounds/bg3.jpg'),
                                   (SCREEN_WIDTH, SCREEN_HEIGHT))
bg4_image = pygame.transform.scale(pygame.image.load('backgrounds/bg4.jpg'),
                                   (SCREEN_WIDTH, SCREEN_HEIGHT))


class Shop:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Shop')
        self.font = pygame.font.Font(None, TEXT_SIZE)

        score_file = open('scores.txt', 'r')
        self.score = int(score_file.read())
        score_file.close()

        self.exit_button = Button("Exit", BUTTON_BG_COLOR, HORIZONTAL_PADDING - 70,
                                  SCREEN_HEIGHT - VERTICAL_PADDING, self.font)
        self.buy_button = Button("Buy", BUTTON_BG_COLOR, SCREEN_WIDTH // 2 - BUTTON_SIZE[0]//2,
                                 SCREEN_HEIGHT - VERTICAL_PADDING, self.font)
        self.left_button = Button("<-", BUTTON_BG_COLOR, HORIZONTAL_PADDING - 70,
                                  SCREEN_HEIGHT // 2 - BUTTON_SIZE[1] //2, self.font)
        self.right_button = Button("->", BUTTON_BG_COLOR, SCREEN_WIDTH - HORIZONTAL_PADDING + 70 - BUTTON_SIZE[0],
                                  SCREEN_HEIGHT // 2 - BUTTON_SIZE[1] // 2, self.font)
        self.image_list = [bg1_image, bg2_image, bg3_image, bg4_image]

        self.image_filenames = {
            bg1_image:"backgrounds/bg1.jpg",
            bg2_image:"backgrounds/bg2.jpg",
            bg3_image:"backgrounds/bg3.jpg",
            bg4_image:"backgrounds/bg4.jpg"
        }
        self.image_prices = {
            bg1_image: 0,
            bg2_image: 100,
            bg3_image: 400,
            bg4_image: 500
        }

        self.image_index = 0
        self.load.prices()
    def load_prices(self):
        prices = []
        price_file = open('prices.txt', 'r')
        for line in price_file.readlines():
            prices.append(int(line))
        price_file.close()

        self.image_prices[bg1_image] = prices[0]
        self.image_prices[bg2_image] = prices[1]
        self.image_prices[bg3_image] = prices[2]
        self.image_prices[bg4_image] = prices[3]

    def change_bg(self, direction):
        if direction == "RIGHT":
            self.image_index = self.image_index + 1 if self.image_index < len(self.image_list) - 1 else 0
        if direction == "LEFT":
            self.image_index = self.image_index - 1 if self.image_index > 0 else len(self.image_list) - 1

    def buy_bg(self):
        current_bg = self.image_list[self.image_index]
        current_price = self.image_prices[current_bg]

        if self.score >= current_price:
            self.score -= current_price

            bg_file = open("bg.txt", 'w')
            bg_file.write(self.image_filenames[current_bg])
            bg_file.close()

            price_file = open("prices.txt", 'w')
            self.image_prices[current_bg] = 0
            for value in self.image_prices.values():
                price_file.write(str(value) + "\n")
            price_file.close()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.exit_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                        return
                    if self.right_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                        self.change_bg("RIGHT")
                    if self.left_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                        self.change_bg("LEFT")
                    if self.buy_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                        self.buy_bg()
                self.screen.blit(self.image_list[self.image_index], (0,0))

                score_text = self.font.render(f"Score: {self.score}", True, TEXT_COLOR,
                                              BUTTON_BG_COLOR)
                self.screen.blit(score_text, (TEXT_PADDING_H, TEXT_PADDING_V))

                price_text = self.font.render(f"Price: {self.image_prices[self.image_list[self.image_index]]}", True,
                                              TEXT_COLOR, BUTTON_BG_COLOR)
                self.screen.blit(price_text, (SCREEN_WIDTH - TEXT_PADDING_H - price_text.get_width(), TEXT_PADDING_V))

                for button in [self.exit_button, self.buy_button, self.left_button, self.right_button]:
                    button.draw(self.screen)

                # Обновляем экран
                pygame.display.flip()