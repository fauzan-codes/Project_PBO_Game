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
        img = pygame.transform.scale(self.assets.title, (300, 80))
        screen.blit(img, (self.width//2 - 150, 100))
        self.draw_center_text(screen, "CLICK TO START", 470, 45)

    def draw_game_over(self, screen):
        img = pygame.transform.scale(self.assets.gameover, (300, 80))
        screen.blit(img, (self.width//2 - 150, 100))

        restart_img = pygame.transform.scale(self.assets.restart, (200, 80))
        restart_rect = restart_img.get_rect(center=(self.width//2, 430))

        screen.blit(restart_img, restart_rect)
        self.restart_rect = restart_rect

    def draw_pause(self, screen):
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(180)
        overlay.fill((0,0,0))
        screen.blit(overlay, (0,0))

        font_big = pygame.font.Font(None, 80)
        text = font_big.render("PAUSED", True, (255,255,255))
        rect = text.get_rect(center=(self.width//2, 200))
        screen.blit(text, rect)

        font_small = pygame.font.Font(None, 40)
        text1 = font_small.render("Press SPACE to Continue", True, (255,255,255))
        text2 = font_small.render("Press R to Restart", True, (255,255,255))

        # resume_img = pygame.transform.scale(self.assets.resume, (200, 80))
        # self.resume_rect = resume_img.get_rect(center=(self.width//2, 350))
        # screen.blit(resume_img, self.resume_rect)

        screen.blit(text1, text1.get_rect(center=(self.width//2, 320)))
        screen.blit(text2, text2.get_rect(center=(self.width//2, 360)))