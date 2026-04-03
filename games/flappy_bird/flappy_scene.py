# .\games\flappy_bird\flappy_scene.py
import pygame
import random
from games.flappy_bird.bird import Bird
from games.flappy_bird.pipe import Pipe
from games.flappy_bird.flappy_assets import FlappyAssets
from games.flappy_bird.flappy_ui import FlappyUI
from games.flappy_bird.flappy_renderer import FlappyRenderer
from games.flappy_bird.flappy_animation import FlappyAnimation


class FlappyScene:
    def __init__(self, width, height, game):
        self.width = width
        self.height = height
        self.game = game

        # SYSTEM
        self.assets = FlappyAssets()
        self.ui = FlappyUI(width, height, self.assets)
        self.renderer = FlappyRenderer(width, height, self.assets)
        self.anim = FlappyAnimation()

        # OBJECT
        self.bird = Bird(self.width // 2 - 20, self.height // 2, self.assets)
        self.pipes = []

        # GAME STATE
        self.state = "HOME"  # HOME | PLAYING | DYING | GAME_OVER
        self.pause = False
        self.game_over_timer = 0

        # SCORE
        self.score = 0
        self.passed_pipes = []

        # PIPE SPAWN
        self.spawn_timer = 0

        # GROUND
        self.ground_y = self.height - self.assets.ground.get_height()

        # SCROLL
        self.bg_x = 0
        self.bg_speed = 1

        self.ground_x = 0
        self.ground_speed = 3


    # ================= INPUT =================
    def handle_event(self, event, rel_mouse=None):
        if event.type == pygame.KEYDOWN:

            # ESC CONTROL
            if event.key == pygame.K_ESCAPE:
                if self.state == "HOME":
                    self.game.game_manager.go_to_menu()

                elif self.state == "PLAYING":
                    self.pause = True

                elif self.state == "GAME_OVER":
                    self.state = "HOME"

                return

            # PAUSE CONTROL
            if self.pause:
                if event.key == pygame.K_SPACE:
                    self.pause = False
                elif event.key == pygame.K_r:
                    self.reset()
                elif event.key == pygame.K_h:
                    self.game.game_manager.go_to_menu()
                return

            # SPACE CONTROL
            if event.key == pygame.K_SPACE:
                if self.state == "HOME":
                    self.state = "PLAYING"
                    self.bird.jump()
                    self.assets.sfx_wing.play()

                elif self.state == "PLAYING":
                    self.bird.jump()
                    self.assets.sfx_wing.play()

            # SHORTCUT
            if event.key == pygame.K_r:
                self.reset()

            if event.key == pygame.K_h:
                self.game.game_manager.go_to_menu()

        # MOUSE (LEFT CLICK ONLY)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.state == "HOME":
                self.state = "PLAYING"

            elif self.state == "GAME_OVER":
                self.reset()


    # ================= UPDATE =================
    def update(self):
        self.assets.update()
        self.anim.update()

        if self.pause:
            return

        # SCROLL (background + ground)
        self.bg_x -= self.bg_speed
        if self.bg_x <= -self.assets.background.get_width():
            self.bg_x = 0

        self.ground_x -= self.ground_speed
        if self.ground_x <= -self.assets.ground.get_width():
            self.ground_x = 0

        # DYING → delay ke game over
        if self.state == "DYING":
            self.game_over_timer += 1
            if self.game_over_timer > 30:
                self.state = "GAME_OVER"
            return

        # HOME (idle animation)
        if self.state == "HOME":
            self.bird.y = self.height // 2 + self.anim.get_idle_offset()
            return

        # PLAYING
        if self.state == "PLAYING":
            self.bird.update()

            # SPAWN PIPE
            self.spawn_timer += 1
            spawn_delay = max(80 - self.score, 50)

            if self.spawn_timer > random.randint(spawn_delay, spawn_delay + 30):
                self.spawn_timer = 0

                height = random.randint(50, self.ground_y - 200)
                gap = max(150 - self.score * 2, 100)

                pipe = Pipe(self.width, height, self.assets, self.ground_y)
                pipe.gap = gap
                pipe.speed = 3 + self.score * 0.1

                self.pipes.append(pipe)

            # UPDATE PIPE
            for pipe in self.pipes:
                pipe.update()

            # CLEAN PIPE
            self.pipes = [p for p in self.pipes if p.x + p.width > 0]

            # COLLISION & SCORE
            bird_rect = self.bird.get_rect()

            for pipe in self.pipes:
                top, bottom = pipe.get_rects()

                if bird_rect.colliderect(top) or bird_rect.colliderect(bottom):
                    self.game_over()

                if pipe not in self.passed_pipes and pipe.x < self.bird.x:
                    self.passed_pipes.append(pipe)
                    self.score += 1
                    self.assets.sfx_swoosh.play()

            # GROUND COLLISION (FIX POSISI)
            bird_height = self.bird.image.get_height()
            if self.bird.y + bird_height >= self.ground_y:
                self.bird.y = self.ground_y - bird_height
                self.game_over()


    # ================= DRAW =================
    def draw(self, screen):
        self.renderer.draw_background(screen, self.bg_x)
        self.renderer.draw_pipes(screen, self.pipes)
        self.renderer.draw_ground(screen, self.ground_x, self.ground_y)
        self.renderer.draw_bird(screen, self.bird)

        # UI
        if self.state == "HOME":
            self.ui.draw_home(screen)

        elif self.state == "PLAYING":
            self.ui.draw_score(screen, self.score)

        elif self.state == "GAME_OVER":
            self.ui.draw_score(screen, self.score)
            self.ui.draw_game_over(screen)

        if self.pause:
            self.ui.draw_pause(screen)


    # ================= GAME LOGIC =================
    def game_over(self):
        if self.state not in ["GAME_OVER", "DYING"]:
            self.state = "DYING"
            self.bird.dead = True
            self.assets.sfx_hit.play()
            self.assets.sfx_die.play()
            self.game_over_timer = 0


    def reset(self):
        self.bird = Bird(self.width // 2 - 20, self.height // 2, self.assets)
        self.pipes = []
        self.passed_pipes = []
        self.spawn_timer = 0
        self.score = 0
        self.state = "HOME"
        self.pause = False