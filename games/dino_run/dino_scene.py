# .\games\dino_run\dino_scene.py
import pygame
import random

from games.dino_run.dino import Dino
from games.dino_run.obstacle import ObstacleManager
from games.dino_run.environment import Environment
from games.dino_run.dino_ui import DinoUI


class DinoScene:
    def __init__(self, width, height, game, assets):
        self.width = width
        self.height = height
        self.game = game
        self.assets = assets

        # === OBJECT ===
        self.env = Environment(width, height, self.assets)
        self.dino = Dino(100, self.env.ground_y - 86 + 18, self.assets)
        self.obstacles = ObstacleManager(width, height, self.assets)
        self.ui = DinoUI(width, height)

        # === STATE ===
        self.state = "HOME"
        self.pause = False

        # === GAME DATA ===
        self.score = 0
        self.speed = 7

        # obstacle spawn delay
        self.spawn_timer = 0

        self.score_timer = 0
        self.last_score_sound = 0

    # ================= INPUT =================
    def handle_event(self, event, rel_mouse=None):
        if event.type == pygame.KEYDOWN:

            # ESC
            if event.key == pygame.K_ESCAPE:
                if self.state == "HOME":
                    from scenes.game_select import GameSelect
                    self.game.game_manager.change_scene(GameSelect(self.game.game_manager))

                elif self.state == "PLAYING":
                    self.pause = True

                elif self.state == "GAME_OVER":
                    self.reset()

                return

            # === PAUSE ===
            if self.pause:
                if event.key == pygame.K_SPACE:
                    self.pause = False
                    self.dino.jump()
                elif event.key == pygame.K_r:
                    self.reset()
                return

            # === GAME OVER ===
            if self.state == "GAME_OVER":
                if event.key == pygame.K_r:
                    self.reset()
                return

            # === CONTROL ===
            if event.key in (pygame.K_SPACE, pygame.K_UP):
                if self.state == "HOME":
                    self.state = "PLAYING"
                    self.dino.jump()

                elif self.state == "PLAYING":
                    self.dino.jump()

            if event.key == pygame.K_DOWN:
                self.dino.duck(True)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.dino.duck(False)

    # ================= UPDATE =================
    def update(self):
        # pause
        if self.pause:
            return

        if self.state == "GAME_OVER":
            return

        # HOME (idle anim)
        if self.state == "HOME":
            self.dino.image = self.assets.dino_jump
            # self.env.update(0) 
            return

        if self.state == "PLAYING":
            # === UPDATE OBJECT ===
            self.dino.update()
            self.env.update(self.speed)
            self.obstacles.update(self.speed, self.score)

            # === COLLISION ===
            if self.obstacles.check_collision(self.dino):
                self.game_over()
                return

            # === SCORE ===
            self.score_timer += 1
            increment_speed = max(3, int(8 - self.speed * 0.5))

            if self.score_timer >= increment_speed:
                self.score += 1
                self.score_timer = 0

            if self.score - self.last_score_sound >= 100:
                self.assets.sfx_score.play()
                self.last_score_sound = self.score

            # === SPEED SCALE ===
            if self.speed < 15:
                self.speed += 0.003
            elif self.speed < 20:
                self.speed += 0.001

    # ================= DRAW =================
    def draw(self, screen):
        screen.fill((255, 255, 255))

        self.env.draw(screen)
        self.obstacles.draw(screen)
        self.dino.draw(screen)

        # === UI ===
        if self.state == "HOME":
            self.ui.draw_home(screen)

        elif self.state in ["PLAYING", "GAME_OVER"]:
            self.ui.draw_score(screen, self.score)

            if self.state == "GAME_OVER":
                self.ui.draw_game_over(screen)

        if self.pause:
            self.ui.draw_pause(screen)

    # ================= GAME LOGIC =================
    def game_over(self):
        if self.state != "GAME_OVER":
            self.state = "GAME_OVER"
            self.dino.die()
            self.assets.sfx_lose.play()

    def reset(self):
        self.__init__(self.width, self.height, self.game, self.assets)