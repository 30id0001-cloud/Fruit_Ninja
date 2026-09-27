import sys

import pygame

from settings import *
from game import Game
from shop import Shop
from button import Button
from knife_shop import KnifeShop

class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fruit Ninja")

        self.logo_name = pygame.transform.scale(
            pygame.image.load("images/logo.png"),
            (int(SCREEN_WIDTH / 1.5), int(SCREEN_HEIGHT / 1.5))
        )
        self.font = pygame.font.Font("Arial", TEXT_SIZE)

        self.game_button = Button("Play", BUTTON_BG_COLOR, HORIZONTAL_PADDING,
                                  VERTICAL_PADDING, self.font)
        self.shop_button = Button("Shop", BUTTON_BG_COLOR, HORIZONTAL_PADDING,
                                  VERTICAL_PADDING * 2 + BUTTON_SIZE[1], self.font)

        self.knife_shop_button = Button("Knives", BUTTON_BG_COLOR, HORIZONTAL_PADDING,
                                        VERTICAL_PADDING * 3 + BUTTON_SIZE[1] * 2, self.font)

        self.exit_button = Button("Exit", BUTTON_BG_COLOR, HORIZONTAL_PADDING,
                                  VERTICAL_PADDING * 4 + BUTTON_SIZE[1] * 3, self.font)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.exit_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        exit()
                    if self.shop_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                        Shop().run()
                    if self.game_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                        Game().run()
                    if self.knife_shop_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                        KnifeShop().run()
            self.screen.fill((18, 18,18))
            self.screen.blit(self.logo_name, (SCREEN_WIDTH // 2 - 100, 100))

            self.game_button.draw(self.screen)
