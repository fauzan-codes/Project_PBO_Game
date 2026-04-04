# Project_PBO_Game\games\snake\food.py
import random
from core.game_object import GameObject

class Food(GameObject):
    def __init__(self, grid_width, grid_height):
        super().__init__(0, 0)

        self.grid_width = grid_width
        self.grid_height = grid_height

        self.position = (0, 0)

    def spawn(self, snake_body):
        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)

            if (x, y) not in snake_body:
                self.position = (x, y)
                break

    def draw(self, surface):
        pass