# .\games\dino_run\dino_ui.py
import pygame


class DinoUI:
    def __init__(self, width, height, assets):
        self.width = width
        self.height = height
        self.assets = assets

        # self.font = pygame.font.Font(None, 40)
        # self.big_font = pygame.font.Font(None, 70)
        self.font = assets.font_small
        self.medium = assets.font_medium
        self.big_font = assets.font_big


    def draw_home(self, screen):
        self.draw_center(screen, "DINO RUN")
        self.draw_small(screen, "Press SPACE to Start", 50)

   
    def draw_score(self, screen, score):
        score_text = self.font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (self.width - 225, 20))

    
    def draw_game_over(self, screen):
        self.draw_center(screen, "GAME OVER")
        self.draw_small(screen, "Press R to Restart", 50)

   
    def draw_pause(self, screen):
        self.draw_center(screen, "PAUSED")
        self.draw_small(screen, "Press SPACE to Continue", 50)

   
   
    def draw_center(self, screen, text):
        txt = self.big_font.render(text, True, (0, 0, 0))
        rect = txt.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(txt, rect)


    def draw_small(self, screen, text, offset):
        txt = self.font.render(text, True, (0, 0, 0))
        rect = txt.get_rect(center=(self.width // 2, self.height // 2 + offset))
        screen.blit(txt, rect)