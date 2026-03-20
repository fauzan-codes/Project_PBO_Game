from core.base_game import BaseGame
from games.snake.snake import Snake
import pygame

class SnakeGame(BaseGame):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 50)
        self.snake = Snake(100, 100, 20)
        self.objects.append(self.snake)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.is_running = False

            if event.key == pygame.K_UP:
                self.snake.direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                self.snake.direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                self.snake.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                self.snake.direction = (1, 0)

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 100, 0))

        super().draw(screen)  # gambar semua object

        text = self.font.render("SNAKE GAME", True, (255, 255, 255))
        screen.blit(text, (200, 250))