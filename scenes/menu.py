import pygame
from games.snake.snake_game import SnakeGame

class Menu:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.Font(None, 50)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                game = SnakeGame()
                self.game_manager.load_game(game)

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))

        title = self.font.render("GAME COLLECTION", True, (255, 255, 255))
        option1 = self.font.render("1. Snake", True, (255, 255, 255))
        option2 = self.font.render("2. Flappy", True, (255, 255, 255))

        screen.blit(title, (100, 50))
        screen.blit(option1, (100, 150))
        screen.blit(option2, (100, 220))