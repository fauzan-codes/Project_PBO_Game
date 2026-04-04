import pygame
import math

class Bird:
    def __init__(self, x, y, assets):
        self.x = x
        self.y = y

        self.assets = assets

        self.dead = False

        self.velocity = 0
        self.gravity = 0.5
        self.jump_power = -8

        self.image = self.assets.get_bird()


    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        if self.y < 0:
            self.y = 0
            self.velocity = 0

        self.image = self.assets.get_bird()


    def update_idle(self):
        self.y += math.sin(pygame.time.get_ticks() * 0.005) * 0.5
        self.image = self.assets.get_bird()


    def jump(self):
        self.velocity = self.jump_power


    def draw(self, screen):
        if self.dead:
            screen.blit(self.assets.bird_die, (self.x, self.y))
        else:
            screen.blit(self.image, (self.x, self.y))


    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))