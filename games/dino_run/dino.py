# .\games\dino_run\dino.py
from core.game_object import GameObject
import pygame

class Dino(GameObject):
    def __init__(self, x, y, assets):
        super().__init__(x, y)

        self.base_y = y
        self.assets = assets

        self.is_jumping = False
        self.is_ducking = False
        self.dead = False

        # === PHYSICS ===
        self.velocity = 0
        self.gravity = 1.2
        self.jump_power = -22
        self.duck_offset = 34 

        # === ANIMATION ===
        self.frame = 0
        self.timer = 0

        # === SIZE ===
        self.run_size = (80, 86)
        self.duck_size = (108, 52)

        self.image = self.assets.dino_run[0]

    # ================= ACTION =================
    def jump(self):
        if not self.is_jumping and not self.dead:
            if self.is_ducking:
                self.duck(False)
                self.y = self.base_y

            self.velocity = self.jump_power
            self.is_jumping = True
            self.assets.sfx_jump.play()

    def duck(self, is_duck):
        if self.dead:
            return
    
        if self.is_jumping:
            return

        if is_duck and not self.is_ducking:
            self.y += self.duck_offset
        elif not is_duck and self.is_ducking:
            self.y -= self.duck_offset

        self.is_ducking = is_duck


    def die(self):
        self.dead = True

    # ================= UPDATE =================
    def update(self):
        if self.dead:
            return

        # === GRAVITY ===
        if self.is_jumping:
            self.velocity += self.gravity
            self.y += self.velocity

            # landing
            if self.y >= self.base_y:
                self.y = self.base_y
                self.velocity = 0
                self.is_jumping = False
                self.y = self.base_y

        # === ANIMATION ===
        self.animate()

    # ================= ANIMATION =================
    def animate(self):
        self.timer += 1

        # JUMP (prioritas)
        if self.is_jumping:
            self.image = self.assets.dino_jump
            return

        # DUCK
        if self.is_ducking:
            if self.timer >= 10:
                self.frame = (self.frame + 1) % 2
                self.timer = 0
            self.image = self.assets.dino_duck[self.frame]
            return

        # RUN
        if self.timer >= 10:
            self.frame = (self.frame + 1) % 2
            self.timer = 0

        self.image = self.assets.dino_run[self.frame]

    # ================= SIZE =================
    def get_size(self):
        return self.duck_size if self.is_ducking else self.run_size

    # ================= COLLISION =================
    def get_rect(self):
        w, h = self.get_size()
        return pygame.Rect(self.x + 10, self.y + 5, w - 20, h - 10)

    # ================= DRAW =================
    def draw(self, screen):
        w, h = self.get_size()
        img = pygame.transform.scale(self.image, (w, h))
        screen.blit(img, (self.x, self.y))