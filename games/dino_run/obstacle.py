# .\games\dino_run\obstacle.py
from core.game_object import GameObject
import pygame
import random

class Obstacle(GameObject):
    def __init__(self, x, y, image):
        super().__init__(x, y)

        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()

    def update(self, speed):
        self.x -= speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(
            self.x + 10,
            self.y + 10,
            self.width - 20,
            self.height - 20
        )
    
    
    

class Bird(Obstacle):
    def __init__(self, x, y, assets):
        self.frames = [
            pygame.transform.scale(f, (f.get_width()*1.7, f.get_height()*1.7))
            for f in assets.bird
        ]
        self.frame = 0
        self.timer = 0

        super().__init__(x, y, self.frames[0])

    def update(self, speed):
        super().update(speed)

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

        self.next_spawn_x = width + random.randint(300, 600)
        self.next_gap = random.randint(300, 500)
        self.last_spawn_x = width

        self.ground_y = height - (assets.ground.get_height() * 2)

    def update(self, speed, score):
        for obs in self.obstacles:
            obs.update(speed)

        # hapus obstacle keluar layar
        self.obstacles = [o for o in self.obstacles if o.x > -100]

        # spawn pertama
        if len(self.obstacles) == 0:
            self.spawn_obstacle(score)
            return

        last = self.obstacles[-1]

        # === BASE GAP ===
        base_min = 500
        base_max = 1000

        # === SPEED SCALING ===
        speed_factor = speed * 30

        min_gap = base_min + int(speed_factor)
        max_gap = base_max + int(speed_factor * 1.5)

        # === RANDOM VARIATION ===
        variation = random.randint(-100, 250)

        required_gap = random.randint(min_gap, max_gap) + variation
        required_gap = max(350, required_gap)

        # === CEK JARAK REAL ===
        distance_to_right = self.width - last.x

        if distance_to_right >= required_gap:
            self.spawn_obstacle(score)

    def spawn_obstacle(self, score):
        x = self.width + 50

        # === BIRD ===
        if score > 400 and random.random() < 0.3:
            y = random.choice([
                self.ground_y - 80,   
                self.ground_y - 120,  
                self.ground_y - 150   
            ])
            self.obstacles.append(Bird(x, y, self.assets))

        # === CACTUS ===
        else:
            img = random.choice(self.assets.cactus)
            img = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
            y = self.ground_y - img.get_height() - 10

            self.obstacles.append(Obstacle(x, y, img))

    def draw(self, screen):
        for obs in self.obstacles:
            obs.draw(screen)

    def check_collision(self, dino):
        dino_rect = dino.get_rect()

        for obs in self.obstacles:
            if dino_rect.colliderect(obs.get_rect()):
                return True
        return False