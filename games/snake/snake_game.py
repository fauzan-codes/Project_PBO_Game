from core.base_game import BaseGame
import pygame

class SnakeGame(BaseGame):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 50)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.is_running = False

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 100, 0))

        text = self.font.render("SNAKE GAME", True, (255, 255, 255))
        screen.blit(text, (200, 250))