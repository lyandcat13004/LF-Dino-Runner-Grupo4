from dino_runner.components.obstacles.obstacle import Obstacle
import random
from dino_runner.utils.constants import (
SMALL_CACTUS
)

class Cactus(Obstacle):
    def __init__(self, image, rect_y=300):
        self.size = 300
        if image == SMALL_CACTUS:
            self.size = 320
    
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.image_rect.y = self.size
        self.image_rect.x = 1000


