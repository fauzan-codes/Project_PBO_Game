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

        self.full_ground = False  
        self.allow_scroll = False

        self.ground_visible_width = 120
        self.target_width = self.width    
        self.expand_speed = 20            
        self.is_expanding = False

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

        # =========================
        # EXPAND
        # =========================
        if self.is_expanding:

            self.ground_visible_width += self.expand_speed

            if self.ground_visible_width >= self.target_width:

                self.ground_visible_width = self.target_width
                self.is_expanding = False

                self.allow_scroll = True
                self.full_ground = True

        # =========================
        # SCROLL
        # =========================
        if self.allow_scroll:

            self.x -= speed

            if self.x <= -self.tile_width:
                self.x = 0

        # =========================
        # CLOUD
        # =========================
        self.spawn_timer += 1

        if self.spawn_timer > random.randint(120, 300):
            self.spawn_cloud()
            self.spawn_timer = 0

        for cloud in self.clouds:
            cloud.update(speed)

        self.clouds = [c for c in self.clouds if c.x > -100]

    def spawn_cloud(self):
        y = random.randint(50, 200)
        x = self.width + 50
        self.clouds.append(Cloud(x, y, self.assets.cloud))


    # =========================
    def draw(self, screen):

        dino_x = 100

        # =========================
        # EXPAND MODE
        # =========================
        if not self.allow_scroll:

            visible_width = int(self.ground_visible_width)

            left = dino_x - (visible_width // 3)
            left = max(0, left)
            right = min(self.width, left + visible_width)

            clip_rect = pygame.Rect(
                left,
                self.ground_y,
                right - left,
                self.ground_height
            )

            screen.set_clip(clip_rect)

            x = 0

            while x < self.width + self.tile_width:
                screen.blit(self.ground_img, (x, self.ground_y))
                x += self.tile_width

            screen.set_clip(None)

        # =========================
        # SCROLL MODE
        # =========================
        else:

            x = self.x

            while x < self.width + self.tile_width:
                screen.blit(self.ground_img, (x, self.ground_y))
                x += self.tile_width

        # =========================
        # CLOUD
        # =========================
        for cloud in self.clouds:
            cloud.draw(screen)