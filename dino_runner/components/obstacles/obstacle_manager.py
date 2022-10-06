import pygame
import random
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
        print(len(self.obstacles))
        if len(self.obstacles) == 0:
            cactus_size = random.randint(1, 2)
            if cactus_size == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif cactus_size == 2:
                self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update()
            print(obstacle.image_rect.x)
            print(obstacle.image_rect.width)

            ##if obstacle.image_rect.x < -obstacle.image_rect.width:
                ##self.obstacles.pop()
            
            if game.dino.dino_rect.colliderect(obstacle.image_rect):
                pygame.time.delay(500)
                game.death_count += 1
                ##self.obstacles.pop()
                ##if game.death_count == 5:
                    ##game.playing = False
                ##print(game.death_count)
                ##break
            
            if obstacle.image_rect.x < 0:
                self.obstacles.pop()
                