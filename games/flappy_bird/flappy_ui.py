# .\games\flappy_bird\flappy_ui.py
import pygame

class FlappyUI:
    def __init__(self, width, height, assets):
        self.width = width
        self.height = height
        self.assets = assets

    def draw_center_text(self, screen, text, y, size=50):
        font = pygame.font.Font(None, size)
        render = font.render(text, True, (255,255,255))
        rect = render.get_rect(center=(self.width//2, y))
        screen.blit(render, rect)

    def draw_score(self, screen, score):
        score_str = str(score)
        total_width = sum(self.assets.numbers[int(d)].get_width() for d in score_str)

        x = self.width // 2 - total_width // 2

        for digit in score_str:
            img = self.assets.numbers[int(digit)]
            screen.blit(img, (x, 50))
            x += img.get_width()

    def draw_home(self, screen):
        title_rect = self.assets.title.get_rect(center=(self.width//2, 150))
        screen.blit(self.assets.title, title_rect)
        self.draw_center_text(screen, "CLICK TO START", 400, 45)

    def draw_game_over(self, screen):
        screen.blit(self.assets.gameover, (self.width//2 - 100, 180))
        self.draw_center_text(screen, "CLICK TO RESTART", 320, 40)
        self.draw_center_text(screen, "R = Restart | H = Home", 360, 30)

    def draw_pause(self, screen):
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(150)
        overlay.fill((0,0,0))
        screen.blit(overlay, (0,0))

        self.draw_center_text(screen, "PAUSED", 250, 60)
        self.draw_center_text(screen, "SPACE = Resume", 320, 40)
        self.draw_center_text(screen, "R = Restart", 360, 40)
        self.draw_center_text(screen, "H = Home", 400, 40)