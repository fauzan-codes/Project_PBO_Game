# .\games\dino_run\environment.py
import pygame
import random


class Cloud:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (92, 26))

    def update(self, speed):
        self.x -= speed * 0.3

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Environment:
    def __init__(self, width, height, assets):
        self.width = width
        self.height = height
        self.assets = assets

        # === GROUND ===
        self.ground_img = pygame.transform.scale(
            assets.ground,
            (assets.ground.get_width() * 2, assets.ground.get_height() * 2)
        )

        self.ground_height = self.ground_img.get_height()
        self.ground_y = self.height - self.ground_height -30

        self.tile_width = self.ground_img.get_width()
        self.tiles = int(self.width / self.tile_width) + 2
        self.x = 0

        # === CLOUD ===
        self.clouds = []
        self.spawn_timer = 0

    # =========================
    def update(self, speed):

        self.x -= speed
        if self.x <= -self.tile_width:
            self.x = 0

        # === CLOUD SPAWN ===
        self.spawn_timer += 1
        if self.spawn_timer > random.randint(120, 300):
            self.spawn_cloud()
            self.spawn_timer = 0

        # update cloud
        for cloud in self.clouds:
            cloud.update(speed)

        # remove off-screen
        self.clouds = [c for c in self.clouds if c.x > -100]

    # =========================
    def spawn_cloud(self):
        y = random.randint(50, 200)
        x = self.width + 50
        self.clouds.append(Cloud(x, y, self.assets.cloud))

    # =========================
    def draw(self, screen):
        for i in range(self.tiles):
            screen.blit(
                self.ground_img,
                (self.x + i * self.tile_width, self.ground_y)
            )

        for cloud in self.clouds:
            cloud.draw(screen)