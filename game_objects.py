from settings import *

apple_img = pygame.image.load("images/apple.png")
orange_img = pygame.image.load("images/orange.png")
watermelon_img = pygame.image.load("images/watermelon.png")
banana_img = pygame.image.load("images/banana.png")

apple_img = pygame.transform.scale(apple_img, OBJECT_SIZE)
orange_img = pygame.transform.scale(orange_img, OBJECT_SIZE)
watermelon_img = pygame.transform.scale(watermelon_img, OBJECT_SIZE)
banana_img = pygame.transform.scale(banana_img, OBJECT_SIZE)



spot_apple_img = pygame.image.load("images/spot_apple.png")
spot_orange_img = pygame.image.load("images/spot_orange.png")
spot_watermelon_img = pygame.image.load("images/spot_watermelon.png")
spot_banana_img = pygame.image.load("images/spot_banana.png")

spot_apple_img = pygame.transform.scale(spot_apple_img, OBJECT_SIZE)
spot_orange_img = pygame.transform.scale(spot_orange_img, OBJECT_SIZE)
spot_watermelon_img = pygame.transform.scale(spot_watermelon_img, OBJECT_SIZE)
spot_banana_img = pygame.transform.scale(spot_banana_img, OBJECT_SIZE)


fruit_to_spot = {

    apple_img : spot_apple_img,
    orange_img : spot_orange_img,
    watermelon_img : spot_watermelon_img,
    banana_img : spot_banana_img
}


class GameObject:
    def  __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - OBJECT_SIZE[0])
        self.y = SCREEN_HEIGHT - 20
        self.gravity = 0.1
        self.size = OBJECT_SIZE
        self.hitbox = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.velocity = [random.randint(-3, 3), random.randint(-10, -5)]

    def move(self):
        self.velocity[1] += self.velocity
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        self.hitbox.x = self.x
        self.hitbox.y = self.y

        if self.x <= 0 or self.x >= SCREEN_WIDTH - OBJECT_SIZE[0]:
            self.velocity[0] *= -1
class Fruit(GameObject):
    def __init__(self):
        super().__init__()
        self.image = random.choice([watermelon_img, banana_img, orange_img, apple_img])
        self.spot_image = fruit_to_spot[self.image]

    def draw(self, screen):
        screen.blit(self.image, self.hitbox)

    def __init__(self):
        self.x = random.randint(0,SCREEN_WIDTH - OBJECT_SIZE(0))
        self.y = SCREEN_HEIGHT - 20

        self.velocity = [random.randint(-3, 3), random.randint(-3, 3)]
        self.gravity = 0.1
        self.size = OBJECT_SIZE
        self.hitbox = pygame.Rect(self.x, self.y, self.size[0], self.size[1])


class Bomb(GameObject):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/bomb.png"),
                                            self.size)
        self.spot_image = pygame.transform.scale(pygame.image.load("images/explode.png"),
                                                 self.size)
    def draw(self, screen):
        screen.blit(self.image, self.hitbox)

class Spot:
    def __init__(self, parent):
        self.parent = parent
        self.lifetime = 60

    def draw(self, screen):
        screen.blit(self.parent.spot_image, self.parent.hitbox)
        self.lifetime -= 1

class KnifeTrail:
    def __init__(self, color, knife_position):
        self.color = color
        self.knife_position = knife_position
        self.lifetime = 20

    def draw(self, screen):
        self.lifetime -= 1
        pygame.draw.rect(screen, self.color, (self.knife_position[0], self.knife_position[1], 5, 5))
