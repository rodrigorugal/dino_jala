import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):

        obstacle_type = [
            Cactus(),
            Cactus()
        ]

        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0, 1)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []