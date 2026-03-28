# Project_PBO_Game\game_manager.py
import pygame

class GameManager:
    def __init__(self):
        self.current_scene = None
        self.current_game = None

        # TRANSITION
        self.is_transitioning = False
        self.transition_alpha = 0
        self.transition_speed = 20
        self.next_scene = None
        self.transition_mode = "in"  # in / out

    def load_game(self, game):
        self.current_game = game

    def unload_game(self):
        self.current_game = None

    def change_scene(self, new_scene):
        self.is_transitioning = True
        self.transition_mode = "out"
        self.transition_alpha = 0
        self.next_scene = new_scene

    def update_transition(self):
        if not self.is_transitioning:
            return

        if self.transition_mode == "out":
            self.transition_alpha += self.transition_speed

            if self.transition_alpha >= 255:
                self.transition_alpha = 255
                self.current_scene = self.next_scene
                self.transition_mode = "in"

        elif self.transition_mode == "in":
            self.transition_alpha -= self.transition_speed

            if self.transition_alpha <= 0:
                self.transition_alpha = 0
                self.is_transitioning = False

    def draw_transition(self, screen):
        if self.is_transitioning:
            overlay = pygame.Surface(screen.get_size())
            overlay.fill((0, 0, 0))
            overlay.set_alpha(self.transition_alpha)
            screen.blit(overlay, (0, 0))