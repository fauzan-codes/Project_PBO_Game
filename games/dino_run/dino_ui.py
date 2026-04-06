# .\games\dino_run\dino_ui.py
import pygame


class DinoUI:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.font = pygame.font.Font(None, 40)
        self.big_font = pygame.font.Font(None, 70)

    # ================= HOME =================
    def draw_home(self, screen):
        self.draw_center(screen, "DINO RUN")
        self.draw_small(screen, "Press SPACE to Start", 50)

    # ================= SCORE =================
    def draw_score(self, screen, score):
        score_text = self.font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (self.width - 200, 20))

    # ================= GAME OVER =================
    def draw_game_over(self, screen):
        self.draw_center(screen, "GAME OVER")
        self.draw_small(screen, "Press R to Restart", 50)

    # ================= PAUSE =================
    def draw_pause(self, screen):
        self.draw_center(screen, "PAUSED")
        self.draw_small(screen, "Press SPACE to Continue", 50)

    # ================= HELPER =================
    def draw_center(self, screen, text):
        txt = self.big_font.render(text, True, (0, 0, 0))
        rect = txt.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(txt, rect)

    def draw_small(self, screen, text, offset):
        txt = self.font.render(text, True, (0, 0, 0))
        rect = txt.get_rect(center=(self.width // 2, self.height // 2 + offset))
        screen.blit(txt, rect)