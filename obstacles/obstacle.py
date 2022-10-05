from email.mime import image
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.image_rect = self.image[self.type].get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.image_rect)

    def update(self):
        self.image_rect.x -= 20
        


        