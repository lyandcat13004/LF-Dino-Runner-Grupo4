from pygame.sprite import Sprite
from dino_runner.utils.constants import BIRD

class Bird(Sprite):
    X_POS = 1000
    Y_POS = 100

    def __init__(self):
        self.image = BIRD[0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = self.X_POS
        self.bird_rect.y = self.Y_POS
        self.bird_run = True
        self.bird_step = 0
        self.flag = 1

    def update(self):
        self.fly()
        if self.bird_step >= 10:
            self.bird_step = 0
        
        if self.X_POS <= -1:
            self.X_POS = 1000

        if self.Y_POS//10 == 0:
            self.flag = self.flag * -1

    def draw(self, screen):
        screen.blit(self.image, (self.bird_rect.x, self.bird_rect.y))
        

    def fly(self):
        self.X_POS -= 1
        self.Y_POS += self.flag
        self.image = BIRD[0] if self.bird_step < 5 else BIRD[1]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = self.X_POS 
        self.bird_rect.y = self.Y_POS
        self.bird_step += 1
