# .\games\flappy_bird\flappy_scene.py
import pygame
import random
from games.flappy_bird.bird import Bird
from games.flappy_bird.pipe import Pipe
from games.flappy_bird.flappy_assets import FlappyAssets
from games.flappy_bird.flappy_ui import FlappyUI
from games.flappy_bird.flappy_renderer import FlappyRenderer


class FlappyScene:
    def __init__(self, width, height, game):
        self.width = width
        self.height = height
        self.game = game

        self.assets = FlappyAssets()
        self.ui = FlappyUI(width, height, self.assets)
        self.renderer = FlappyRenderer(width, height, self.assets)

        # bird
        self.bird = Bird(self.width // 2 - 20, self.height // 2, self.assets)
        self.pipes = []

        # status
        self.state = "HOME"
        self.pause = False
        self.game_over_timer = 0

        # score
        self.score = 0
        self.passed_pipes = []

        # pipe
        self.spawn_timer = 0

        # bg
        self.ground_y = self.height - self.assets.ground.get_height()
        self.bg_x = 0
        self.bg_speed = 1

        self.ground_x = 0
        self.ground_speed = 3
        self.idle_jump_timer = 0


    # ================= INPUT =================
    def handle_event(self, event, rel_mouse=None):
        if event.type == pygame.KEYDOWN:

            # escape
            if event.key == pygame.K_ESCAPE:
                if self.state == "HOME":
                    from scenes.game_select import GameSelect
                    self.game.game_manager.change_scene(GameSelect(self.game.game_manager))

                elif self.state == "PLAYING":
                    self.pause = True

                elif self.state == "GAME_OVER":
                    self.reset()

                return
            

            # pause 
            if self.pause:
                if event.key == pygame.K_SPACE:
                    self.pause = False
                    self.bird.jump()
                    self.assets.sfx_wing.play()
                elif event.key == pygame.K_r:
                    self.reset()
                return
            
            if self.state == "GAME_OVER":
                if event.key == pygame.K_r:
                    self.reset()
                return

            # space kb
            if event.key == pygame.K_SPACE:
                if self.state == "HOME":
                    self.state = "PLAYING"
                    self.bird.jump()
                    self.assets.sfx_wing.play()

                elif self.state == "PLAYING":
                    self.bird.jump()
                    self.assets.sfx_wing.play()


        # mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if rel_mouse is None:
                return
            
            mouse_pos = rel_mouse

            if self.pause:
                # if hasattr(self.ui, "resume_rect") and self.ui.resume_rect.collidepoint(mouse_pos):
                #     self.state = "PLAYING"
                #     self.bird.jump()
                #     self.assets.sfx_wing.play()
                # elif hasattr(self.ui, "restart_rect") and self.ui.restart_rect.collidepoint(mouse_pos):
                #     self.reset()
                return

            if self.state == "GAME_OVER":
                if hasattr(self.ui, "restart_rect") and self.ui.restart_rect.collidepoint(mouse_pos):
                    self.reset()
                return

            if self.state == "HOME":
                self.state = "PLAYING"
                self.bird.jump()
                self.assets.sfx_wing.play()

            elif self.state == "PLAYING":
                self.bird.jump()
                self.assets.sfx_wing.play()


    # ================= UPDATE =================
    def update(self):
        self.assets.update()

        # pause
        if self.pause:
            self.bird.update_idle()
            return

        if self.state == "DYING":
            self.game_over_timer += 1

            if self.game_over_timer > 30:
                self.state = "GAME_OVER"

            return

        if self.state == "GAME_OVER":
            return

        # bg
        self.bg_x -= self.bg_speed
        if self.bg_x <= -self.assets.background.get_width():
            self.bg_x = 0

        self.ground_x -= self.ground_speed
        if self.ground_x <= -self.assets.ground.get_width():
            self.ground_x = 0

        if self.state == "HOME":
            self.bird.update_idle()
            return

        if self.state == "PLAYING":
            self.bird.update()

            # SPAWN PIPE
            self.spawn_timer += 1
            # spawn_delay = 80
            # spawn_delay = max(50, 80 - self.score // 2)  #berdasarkan score
            spawn_delay = random.randint(80, 110)  #random pipe

            if self.spawn_timer > spawn_delay:
                self.spawn_timer = 0

                height = random.randint(100, self.ground_y - 250)
                pipe = Pipe(self.width, height, self.assets, self.ground_y)
                # pipe.gap = 140
                pipe.gap = max(110, 140 - self.score)
                self.pipes.append(pipe)

            for pipe in self.pipes:
                pipe.update()

            self.pipes = [p for p in self.pipes if p.x + p.width > 0] #clean
            bird_rect = self.bird.get_rect() #collision

            for pipe in self.pipes:
                top, bottom = pipe.get_rects()

                if bird_rect.colliderect(top) or bird_rect.colliderect(bottom):
                    self.game_over()
                    break

                if pipe not in self.passed_pipes and pipe.x < self.bird.x:
                    self.passed_pipes.append(pipe)
                    self.score += 1
                    self.assets.sfx_swoosh.play()

            # ground collision
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

        elif self.state in ["PLAYING", "DYING", "GAME_OVER"]:
            self.ui.draw_score(screen, self.score)

            if self.state == "GAME_OVER":
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