import random
import pygame
from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.points = 0
        self.option_numbers = list(range(1, 10))

    def reset_power_ups(self, points):
        self.power_ups = []
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points

    def generator_power_ups(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                print("generating powerup")
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                self.power_ups.append(Shield())
        return self.power_ups
        
    def update(self, points, game_speed, player):
        self.generator_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)