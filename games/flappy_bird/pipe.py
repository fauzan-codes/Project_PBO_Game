# .\games\flappy_bird\pipe.py
import pygame
import random

class Pipe:
    def __init__(self, x, height, assets, ground_y):
        self.assets = assets
        self.x = x
        
        self.ground_y = ground_y
        self.height = height
        self.width = self.assets.pipe.get_width()
        self.gap = 150
        self.min_height = 50
        self.speed = 3



    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        pipe_img = self.assets.pipe
        bottom_y = self.height + self.gap
        if bottom_y > self.ground_y - 50:
            bottom_y = self.ground_y - 50

        # atas
        top_pipe = pygame.transform.flip(pipe_img, False, True)
        screen.blit(top_pipe, (self.x, self.height - pipe_img.get_height()))

        # bawah
        screen.blit(pipe_img, (self.x, bottom_y))

    def get_rects(self):
        pipe_img = self.assets.pipe

        top_rect = pygame.Rect(
            self.x,
            self.height - pipe_img.get_height(),
            pipe_img.get_width(),
            pipe_img.get_height()
        )

        bottom_rect = pygame.Rect(
            self.x,
            self.height + self.gap,
            pipe_img.get_width(),
            pipe_img.get_height()
        )

        return top_rect, bottom_rect