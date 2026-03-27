import pygame

class SnakeUI:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.font_big = pygame.font.Font(None, 80)
        self.font_medium = pygame.font.Font(None, 55)
        self.font = pygame.font.Font(None, 35)

        self.easy = pygame.Rect(0, 0, 200, 60)
        self.easy.center = (width//2, height//2)

        self.medium = pygame.Rect(0, 0, 200, 60)
        self.medium.center = (width//2, height//2 + 80)

        self.hard = pygame.Rect(0, 0, 200, 60)
        self.hard.center = (width//2, height//2 + 160)

        self.btn_resume = pygame.Rect(0, 0, 200, 60)
        self.btn_restart = pygame.Rect(0, 0, 200, 60)
        self.btn_home = pygame.Rect(0, 0, 200, 60)

        self.btn_resume.center = (width//2, height//2)
        self.btn_restart.center = (width//2, height//2 + 80)
        self.btn_home.center = (width//2, height//2 + 160)

    def draw_button(self, surface, rect, text, mouse_pos):
        color = (200,200,200)
        if mouse_pos and rect.collidepoint(mouse_pos):
            color = (255,255,0)

        pygame.draw.rect(surface, color, rect, border_radius=10)

        txt = self.font.render(text, True, (0,0,0))
        surface.blit(txt, txt.get_rect(center=rect.center))


    def draw_side_panel(self, surface, x, y, width, height, score, level, time_played):
        pygame.draw.rect(surface, (40,40,60), (x, y, width, height), border_radius=10)

        # title
        title = self.font.render("SNAKE", True, (255,255,0))
        surface.blit(title, (x+50, y+10))

        # score
        score_text = self.font.render(f"Score: {score}", True, (255,255,255))
        surface.blit(score_text, (x+20, y+60))

        # level
        level_text = self.font.render(f"Level: {level}", True, (255,255,255))
        surface.blit(level_text, (x+20, y+100))

        # time
        minutes = time_played // 60
        seconds = time_played % 60

        time_text = self.font.render(f"Time: {minutes:02}:{seconds:02}", True, (255,255,255))
        surface.blit(time_text, (x+20, y+140))

    def draw_pause_menu(self, surface, mouse_pos):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0,0,0,150))
        surface.blit(overlay, (0,0))

        title = self.font_big.render("PAUSED", True, (255,255,255))
        surface.blit(title, (self.width//2 - title.get_width()//2, 150))

        self.draw_button(surface, self.btn_resume, "RESUME", mouse_pos)
        self.draw_button(surface, self.btn_restart, "RESTART", mouse_pos)
        self.draw_button(surface, self.btn_home, "HOME", mouse_pos)

    def draw_game_over(self, surface, score, time_played, mouse_pos):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0,0,0,180))
        surface.blit(overlay, (0,0))

        title = self.font_big.render("GAME OVER", True, (255, 100, 100))
        surface.blit(title, (self.width//2 - title.get_width()//2, 120))

        # info
        score_text = self.font.render(f"Score : {score}", True, (255,255,255))
        minutes = time_played // 60
        seconds = time_played % 60

        time_text = self.font.render(f"Time : {minutes:02}:{seconds:02}", True, (255,255,255))
        score_x = self.width // 2 - score_text.get_width() // 2
        time_x = self.width // 2 - time_text.get_width() // 2

        surface.blit(score_text, (score_x, 250))
        surface.blit(time_text, (time_x, 300))

        # buttons
        self.draw_button(surface, self.btn_restart, "RESTART", mouse_pos)
        self.draw_button(surface, self.btn_home, "HOME", mouse_pos)