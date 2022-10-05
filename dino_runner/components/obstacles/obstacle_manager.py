from components.obstacles.cactus import Cactus
from utils.constants import LARGE_CACTUS

class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def update(self):
        print(len(self.obstacles))
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(LARGE_CACTUS[1]))

        for obstacle in self.obstacles:
            obstacle.update()