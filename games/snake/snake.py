from core.game_object import GameObject
import pygame

class Snake(GameObject):
    def __init__(self, x, y, size):
        super().__init__(x, y)
        self.size = size
        self.body = [(x, y)]
        self.direction = (1, 0)  # kanan

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction

        new_head = (head_x + dx * self.size, head_y + dy * self.size)
        self.body.insert(0, new_head)
        self.body.pop()

    def update(self):
        self.move()

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (*segment, self.size, self.size))