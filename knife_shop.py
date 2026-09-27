from settings import *
from button import Button


class KnifeShop:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Knife Shop")
        self.font = pygame.font.Font(None, TEXT_SIZE)

        score_file = open("score.txt", "r")
        self.score = int(score_file.read())
        score_file.close()

        self.exit_button = Button("Exit", BUTTON_BG_COLOR, HORIZONTAL_PADDING - 70, SCREEN_HEIGHT - VERTICAL_PADDING,
                                  self.font)
        self.buy_button = Button("Buy", BUTTON_BG_COLOR, SCREEN_WIDTH // 2 - BUTTON_SIZE[0] // 2,
                                 SCREEN_HEIGHT - VERTICAL_PADDING, self.font)
        self.left_button = Button("<-", BUTTON_BG_COLOR, HORIZONTAL_PADDING - 70,
                                  SCREEN_HEIGHT // 2 - BUTTON_SIZE[1] // 2, self.font)
        self.right_button = Button("->", BUTTON_BG_COLOR, SCREEN_WIDTH - HORIZONTAL_PADDING + 70 - BUTTON_SIZE[0],
                                   SCREEN_HEIGHT // 2 - BUTTON_SIZE[1] // 2, self.font)

        self.image_list = [
            (255,0,0),
            (0,255,0),
            (0,0,255),
            (255,255,0)
        ]

        self.image_prices = {
            (255, 0, 0) : 0,
            (0, 255, 0) : 100,
            (0, 0, 255) : 200,
            (255, 255, 0) : 1000
        }

        self.image_index = 0

    def change_bg(self, direction):
        if direction == "RIGHT":
            self.image_index = self.image_index + 1 if self.image_index < len(self.image_list) - 1 else 0
        if direction == "LEFT":
            self.image_index = self.image_index - 1 if self.image_index > 0 else len(self.image_list) - 1

    def buy_bg(self):
        current_color = self.image_list[self.image_index]
        current_price = self.image_prices[current_color]

        if self.score >= current_price:
            self.score -= current_price
            bg_file = open("knife_color.txt", "w")
            bg_file.write(self.image_filenames[current_color])
            bg_file.close()

            score_file = open("score.txt", "w")
            score_file.write(str(self.score))
            score_file.close()

    def run(self):
        while True:
            for event in pygame.event.get():
                # Выход из игры
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # Обработка кликов мыши по кнопкам
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.exit_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                        return  # Возврат в главное меню
                    if self.right_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                        self.change_bg("RIGHT")
                    if self.left_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                        self.change_bg("LEFT")
                    if self.buy_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                        self.buy_bg()

            # ------------------------
            # ОТРИСОВКА ЭКРАНА МАГАЗИНА
            # ------------------------

            # Закрашиваем прямоугольную область текущим выбранным цветом (превью ножа)
            self.screen.fill((0, 0, 0))  # очищаем экран
            pygame.draw.rect(self.screen, self.image_list[self.image_index], (250, 100, 300, 300))

            # Отображаем количество очков игрока
            score_text = self.font.render(f"Score: {self.score}", True, TEXT_COLOR, BUTTON_BG_COLOR)
            self.screen.blit(score_text, (TEXT_PADDING_H, TEXT_PADDING_V))

            # Отображаем цену выбранного цвета
            price_text = self.font.render(f"Price: {self.image_prices[self.image_list[self.image_index]]}", True,
                                          TEXT_COLOR, BUTTON_BG_COLOR)
            self.screen.blit(price_text, (SCREEN_WIDTH - TEXT_PADDING_H - price_text.get_width(), TEXT_PADDING_V))

            # Отрисовываем все кнопки интерфейса
            for button in [self.exit_button, self.buy_button, self.left_button, self.right_button]:
                button.draw(self.screen)

            # Обновляем изображение на экране
            pygame.display.flip()