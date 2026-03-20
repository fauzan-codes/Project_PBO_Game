import pygame
from games.snake.snake_game import SnakeGame

class GameSelect:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.Font(None, 40)

        self.games = [
            {"name": "Snake", "class": SnakeGame},
            {"name": "Flappy", "class": None},
            {"name": "Game 3", "class": None},
            {"name": "Game 4", "class": None},
            {"name": "Game 5", "class": None},
        ]

        self.selected = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.selected = (self.selected + 1) % len(self.games)
            elif event.key == pygame.K_LEFT:
                self.selected = (self.selected - 1) % len(self.games)

            elif event.key == pygame.K_RETURN:
                game_class = self.games[self.selected]["class"]
                if game_class:
                    game = game_class()
                    self.game_manager.load_game(game)

            elif event.key == pygame.K_ESCAPE:
                from scenes.home import Home
                self.game_manager.current_scene = Home(self.game_manager)

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((30, 30, 40))

        for i, game in enumerate(self.games):
            x = 150 + i * 200
            y = 200

            color = (200, 200, 200)
            if i == self.selected:
                color = (255, 255, 0)

            pygame.draw.rect(screen, color, (x, y, 150, 200), border_radius=10)

            text = self.font.render(game["name"], True, (0, 0, 0))
            screen.blit(text, (x + 30, y + 80))