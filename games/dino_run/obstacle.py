# .\games\dino_run\obstacle.py
import pygame
import random


class Obstacle():
    def __init__(self, x, y, image, width, height):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)

    def update(self, speed):
        self.x -= speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Bird(Obstacle):
    def __init__(self, x, y, assets):
        self.frames = [
            pygame.transform.scale(assets.bird[0], (84, 62)),
            pygame.transform.scale(assets.bird[1], (84, 62)),
        ]

        self.frame = 0
        self.timer = 0

        super().__init__(x, y, self.frames[0], 84, 62)

    def update(self, speed):
        super().update(speed)

        # animasi sayap
        self.timer += 1
        if self.timer >= 10:
            self.frame = (self.frame + 1) % 2
            self.image = self.frames[self.frame]
            self.timer = 0


class ObstacleManager:
    def __init__(self, width, height, assets):
        self.width = width
        self.height = height
        self.assets = assets

        self.obstacles = []
        self.spawn_timer = 0

    # =========================
    def update(self, speed, score):
        self.spawn_timer += 1

        # spawn delay random
        if self.spawn_timer > random.randint(60, 120):
            self.spawn_obstacle(score)
            self.spawn_timer = 0

        for obs in self.obstacles:
            obs.update(speed)

        self.obstacles = [o for o in self.obstacles if o.x > -100]

    # =========================
    def spawn_obstacle(self, score):
        x = self.width + 50

        if score > 400 and random.random() < 0.3:
            height_type = random.choice(["low", "mid", "high"])

            if height_type == "low":
                y = self.height - 100
            elif height_type == "mid":
                y = self.height - 140
            else:
                y = self.height - 180

            self.obstacles.append(Bird(x, y, self.assets))

        else:
            img = random.choice(self.assets.cactus)

            # pakai size asli image
            w, h = img.get_width(), img.get_height()

            y = self.height - h - 20

            self.obstacles.append(
                Obstacle(x, y, img, w, h)
            )

    # =========================
    def draw(self, screen):
        for obs in self.obstacles:
            obs.draw(screen)

    # =========================
    def check_collision(self, dino):
        dino_rect = dino.get_rect()

        for obs in self.obstacles:
            if dino_rect.colliderect(obs.rect):
                return True
        return False