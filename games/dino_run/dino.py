# .\games\dino_run\dino.py
import pygame

class Dino:
    IDLE = 0
    RUN = 1
    JUMP = 2
    DUCK = 3
    DEAD = 4

    def __init__(self, x, y, assets):
        self.x = x
        self.y = y
        self.base_y = y

        self.assets = assets

        # === STATE ===
        self.state = self.IDLE

        # === PHYSICS ===
        self.vel_y = 0
        self.gravity = 0.8
        self.jump_force = -15

        # === ANIMATION ===
        self.frame = 0
        self.anim_timer = 0

        # === SIZE ===
        self.width = 80
        self.height = 86

        self.duck_width = 108
        self.duck_height = 52

        # === CURRENT IMAGE ===
        self.image = self.assets.dino_run[0]

    # =========================
    # ACTION
    # =========================
    def jump(self):
        if self.state != self.JUMP:
            self.vel_y = self.jump_force
            self.state = self.JUMP
            self.assets.sfx_jump.play()

    def duck(self, is_ducking):
        if is_ducking and self.state != self.JUMP:
            self.state = self.DUCK
        elif not is_ducking and self.state == self.DUCK:
            self.state = self.RUN

    def die(self):
        self.state = self.DEAD

    # =========================
    # UPDATE
    # =========================
    def update(self):
        # === GRAVITY ===
        if self.state == self.JUMP:
            self.vel_y += self.gravity
            self.y += self.vel_y

            # landing
            if self.y >= self.base_y:
                self.y = self.base_y
                self.vel_y = 0
                self.state = self.RUN

        # === AUTO RUN ===
        if self.state == self.IDLE:
            return
        elif self.state not in (self.JUMP, self.DUCK, self.DEAD):
            self.state = self.RUN

        # === ANIMATION ===
        self.animate()

    # =========================
    def animate(self):
        self.anim_timer += 1

        # RUN animation
        if self.state == self.RUN:
            if self.anim_timer >= 10:
                self.frame = (self.frame + 1) % 2
                self.anim_timer = 0

            self.image = self.assets.dino_run[self.frame]

        # DUCK animation
        elif self.state == self.DUCK:
            if self.anim_timer >= 5:
                self.frame = (self.frame + 1) % 2
                self.anim_timer = 0

            self.image = self.assets.dino_duck[self.frame]

        # JUMP image
        elif self.state == self.JUMP:
            self.image = self.assets.dino_jump

        # IDLE (pakai jump image biar diam)
        elif self.state == self.IDLE:
            self.image = self.assets.dino_jump

    # =========================
    # DRAW
    # =========================
    def draw(self, screen):
        w, h = self.get_size()
        img = pygame.transform.scale(self.image, (w, h))
        y_offset = self.base_y + (43 - h)
        screen.blit(img, (self.x, y_offset))

    # =========================
    def get_size(self):
        if self.state == self.DUCK:
            return (self.duck_width, self.duck_height)
        return (self.width, self.height)

    # =========================
    def get_rect(self):
        w, h = self.get_size()
        return pygame.Rect(self.x, self.y, w, h)