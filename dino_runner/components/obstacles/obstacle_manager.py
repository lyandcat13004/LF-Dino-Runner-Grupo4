import pygame
import random
from dino_runner.components.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import (
LARGE_CACTUS, SMALL_CACTUS
)

class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = random.randint(0, 2)
            if obstacle_type == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif obstacle_type == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self.obstacles.append(Bird())


        for obstacle in self.obstacles:
            obstacle.update()
            if isinstance(obstacle, Bird):
                obstacle.fly()
        
            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()
            
            if game.dino.dino_rect.colliderect(obstacle.image_rect):
                pygame.time.delay(500)
                game.death_count += 1
                self.obstacles.pop()
                if game.death_count == 5:
                    game.playing = False
                    game.execute()
                print(game.death_count)
            
            
          
                