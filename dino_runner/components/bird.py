from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
import random


class Bird(Obstacle):
    X_POS = 1000
    Y_POS = 100

    def __init__(self):
        self.type = random.randint(0, 1)
        super().__init__(BIRD, self.type)
        self.image_rect.x = self.X_POS
        self.image_rect.y = self.Y_POS
        self.flag = 1
        self.bird_step = 0
    

    def fly(self):
        self.Y_POS += self.flag
        self.image = BIRD[0] if self.bird_step < 5 else BIRD[1]
        self.image_rect.y = self.Y_POS
        self.bird_step += 1
        if self.bird_step >= 10:
            self.bird_step = 0
        
        if self.Y_POS % 10 == 0:
            self.flag = self.flag * -1
