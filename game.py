from settings import *
from game_objects import Fruit, Bomb, Spot, KnifeTrail
from button import Button

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fruit Ninja")
        pygame.mouse.set_visible(False)

        self.knife_img = pygame.transform.scale(pygame.image.load("images/knife.png"),
                                                OBJECT_SIZE)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, TEXT_SIZE)

        self.game_objects = []
        self.spots = []

        score_file = open("score.txt", "r")
        self.score = int(score_file.read())
        score_file.close()

        self.lives = 3
        self.heart_img = pygame.transform.scale(pygame.image.load("images/heart.png"),
                                                OBJECT_SIZE)
        self.go_button = Button("Menu", BUTTON_BG_COLOR, (SCREEN_WIDTH - BUTTON_SIZE[0]) // 2, SCREEN_HEIGHT // 2 - 200,
                                self.font)
        bg_file = open("bg.txt", "r")
        bg_name = bg_file.read()
        bg_file.close()
        self.bg_image = pygame.transform.scale(pygame.image.load(bg_name), (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.knife_color = (0,255,0)
        self.knife_trail = []

        color_file = open("knife_color.txt")
        self.knife_color = color_file.read()
        color_file.close()

        self.exit_button = Button("Exit", BUTTON_BG_COLOR, HORIZONTAL_PADDING,
                                  VERTICAL_PADDING * 4 + BUTTON_SIZE[1] * 3, self.font)

    def save_score(self):
        score_file = open("score.txt", "w")
        score_file.write(str(self.score))
        score_file.close()

    def game_over(self):
        pygame.mouse.set_visible(False)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.score = 0
                    self.save_score()
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.go_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                        self.score = 0
                        self.save_score()
                        return
            go_text = self.font.render("GAME OVER", True, (255, 0, 0))
            self.screen.blit(go_text,
                             ((SCREEN_WIDTH - go_text.get_width()) // 2,
                              (SCREEN_HEIGHT - go_text.get_height()) // 2))
            self.go_button.draw(self.screen)
            pygame.display.flip()

    def run(self):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.save_score()
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.exit_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                            pygame.mouse.set_visible(True)
                            return
                if self.lives <= 0:
                    self.game_over()
                    return

                if random.random() < 0.01:
                    if random.random() < 0.8:
                        self.game_objects.append(Fruit())
                    else:
                        self.game_objects.append(Bomb())

                self.screen.blit(self.bg_image, (0,0))
                self.exit_button.draw(self.screen)

                for game_object in self.game_objects:
                    game_object.draw(self.screen)
                    game_object.move()

                    if game_object.hitbox.collidepoint(pygame.mouse.get_pos()):
                        self.spots.append(Spot(game_object))
                        self.game_objects.remove(game_object)
                        if isinstance(game_object, Fruit):
                            self.score += 1
                        else:
                            self.lives -= 1

                    if game_object.y > SCREEN_HEIGHT:
                        self.game_objects.remove(game_object)
                        if isinstance(game_object, Fruit):
                            self.lives -= 1
                for spot in self.spots:
                    spot.draw(self.screen)
                    if spot.lifetime <= 0 :
                        self.spots.remove(spot)
                for i in range(self.lives):
                    self.screen.blit(self.heart_img, (SCREEN_WIDTH-200 + i*OBJECT_SIZE[0], TEXT_PADDING_V))

                self.screen.blit(self.knife_img, pygame.mouse.get_pos())

                self.knife_trail.append(KnifeTrail(self.knife_color, pygame.mouse.get_pos()))
                for trail_piece in self.knife_trail:
                    trail_piece.draw(self.screen)
                    if trail_piece.lifetime <= 0:
                        self.knife_trail.remove(trail_piece)
                score_text = self.font.render(f"Score: {self.score}", True, TEXT_COLOR,
                                              BUTTON_BG_COLOR)
                self.screen.blit(score_text, (TEXT_PADDING_H, TEXT_PADDING_V))

                pygame.display.flip()
                self.clock.tick(FPS)
