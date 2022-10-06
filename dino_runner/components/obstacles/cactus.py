from dino_runner.components.obstacles.obstacle import Obstacle
import random

class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.image_rect.y = 325
        self.image_rect.x = 1000
