# Project_PBO_Game\games\snake\snake_game.py
import pygame
from core.base_game import BaseGame
from games.snake.snake_scene import SnakeScene
from games.snake.snake_assets import SnakeAssets

class SnakeGame(BaseGame):
    def __init__(self, game_manager):
        super().__init__()

        self.game_manager = game_manager

        # screen
        self.screen = pygame.display.get_surface()
        self.width, self.height = self.screen.get_size()

        # UI AREA //
        self.header_height = 60

        # game window area
        self.game_width = 800
        self.game_height = 600

        self.game_surface = pygame.Surface((self.game_width, self.game_height))
        self.fullscreen = False

        self.calculate_layout()
        self.scene = SnakeScene(self.game_width, self.game_height, self)
        self.assets = SnakeAssets()

        # scroll
        self.scroll_y = 0

        # font
        self.font = pygame.font.Font(None, 40)
        self.small_font = pygame.font.Font(None, 28)

    # ==================== LAYOUT SYSTEM ====================
    def calculate_layout(self):
        ratio = 4 / 3

        # fullscreen
        if self.fullscreen:
            available_width = self.width
            available_height = self.height - self.header_height

            new_height = available_height
            new_width = int(new_height * ratio)

            if new_width > available_width:
                new_width = available_width
                new_height = int(new_width / ratio)

            # center
            x = (self.width - new_width) // 2
            y = self.header_height + (available_height - new_height) // 2

            self.game_rect = pygame.Rect(x, y, new_width, new_height)

        # window
        else:
            new_width = self.game_width
            new_height = self.game_height

            x = (self.width - new_width) // 2
            y = self.header_height + 20

            self.game_rect = pygame.Rect(x, y, new_width, new_height)

        # header
        self.header_rect = pygame.Rect(0, 0, self.width, self.header_height)

        # info 
        if not self.fullscreen:
            info_height = len(self._get_info_text()) * 30 + 20
            self.info_rect = pygame.Rect(
                0,
                self.game_rect.bottom + 10,
                self.width,
                info_height
            )
        else:
            self.info_rect = None

    # ==================== BUTTON EVENT ====================
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                self.toggle_fullscreen()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            # button back
            if hasattr(self, "back_rect") and self.back_rect.collidepoint(mouse_pos):
                pygame.mixer.music.stop()
                from scenes.game_select import GameSelect
                self.game_manager.change_scene(GameSelect(self.game_manager))

            # button fullscreen
            if hasattr(self, "fullscreen_rect") and self.fullscreen_rect.collidepoint(mouse_pos):
                self.toggle_fullscreen()


        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse_pos = pygame.mouse.get_pos()

            # scroll event
            if event.button == 4:
                self.scroll_y += 20
            elif event.button == 5:
                self.scroll_y -= 20

            self.scroll_event()

        # posisi mouse di game area
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = pygame.mouse.get_pos()

            # posisi game area
            inner_rect = self.game_rect.inflate(-10, -10)
            inner_rect.y += self.scroll_y

            if inner_rect.collidepoint(mx, my):
                rel_x = (mx - inner_rect.x) * (self.game_width / inner_rect.width)
                rel_y = (my - inner_rect.y) * (self.game_height / inner_rect.height)

                self.scene.handle_event(event, (rel_x, rel_y))
        else:
            mx, my = pygame.mouse.get_pos()

            inner_rect = self.game_rect.inflate(-10, -10)
            inner_rect.y += self.scroll_y

            rel_mouse = None

            if inner_rect.collidepoint(mx, my):
                rel_x = (mx - inner_rect.x) * (self.game_width / inner_rect.width)
                rel_y = (my - inner_rect.y) * (self.game_height / inner_rect.height)
                rel_mouse = (rel_x, rel_y)

            self.scene.handle_event(event, rel_mouse)

    def scroll_event(self):
        content_height = self.get_content_height()

        min_scroll = min(0, self.height - content_height)
        max_scroll = 0

        if self.scroll_y < min_scroll:
            self.scroll_y = min_scroll
        if self.scroll_y > max_scroll:
            self.scroll_y = max_scroll

    # ==================== UPDATE ====================
    def update(self):
        super().update()
        self.scene.update()

    def get_content_height(self):
        if self.fullscreen:
            return self.height

        # tinggi teks info
        line_height = 30
        total_lines = len(self._get_info_text())

        info_content_height = total_lines * line_height + 20

        return (
            self.header_height +
            20 +
            self.game_height +
            10 +
            info_content_height
        )



    # ==================== UI ====================
    def draw(self, screen):
        screen.fill((30, 30, 40))
        self.draw_game_area(screen)

        if not self.fullscreen:
            self.draw_info(screen)

        self.draw_header(screen)


    def draw_game_area(self, screen):
        rect = self.game_rect.copy()
        rect.y += self.scroll_y

        
        shadow = rect.copy()
        shadow.y += 6
        pygame.draw.rect(screen, (50, 50, 50), shadow, border_radius=5)

        # border
        pygame.draw.rect(screen, (200, 200, 200), rect, border_radius=5)
        inner_rect = rect.inflate(-10, -10)

        self.game_surface.fill((0, 0, 0))
        self.scene.draw(self.game_surface)

        scaled_surface = pygame.transform.smoothscale(
            self.game_surface,
            (inner_rect.width, inner_rect.height)
        )

        screen.blit(scaled_surface, (inner_rect.x, inner_rect.y))

    # ==================== HEADER ====================
    def draw_header(self, screen):
        shadow = self.header_rect.copy()
        shadow.y += 1
        pygame.draw.rect(screen, (50, 50, 50), shadow)
        pygame.draw.rect(screen, (40, 40, 60), self.header_rect)

        # title
        title = self.font.render("SNAKE GAME", True, (255, 255, 255))
        screen.blit(title, (self.width // 2 - title.get_width() // 2, 15))

        # back button
        self.back_rect = pygame.Rect(20, 10, 100, 40)
        self.draw_button(screen, self.back_rect, "BACK")

        # fullscreen button
        text = "WINDOW" if self.fullscreen else "FULL"
        self.fullscreen_rect = pygame.Rect(self.width - 120, 10, 100, 40)
        self.draw_button(screen, self.fullscreen_rect, text)


    def draw_button(self, screen, rect, text):
        mouse_pos = pygame.mouse.get_pos()

        color = (200, 200, 200)
        if rect.collidepoint(mouse_pos):
            color = (255, 255, 0)

        shadow = rect.copy()
        shadow.y += 4
        pygame.draw.rect(screen, (50, 50, 50), shadow, border_radius=10)

        # button
        pygame.draw.rect(screen, color, rect, border_radius=10)

        txt = self.small_font.render(text, True, (0, 0, 0))
        text_rect = txt.get_rect(center=rect.center)
        screen.blit(txt, text_rect)

    # ===================== INFO ====================
    def draw_info(self, screen):
        rect = self.info_rect.copy()
        rect.y += self.scroll_y

        shadow = rect.copy()
        shadow.y += 5
        pygame.draw.rect(screen, (50, 50, 50), shadow, border_radius=10)

        # panel
        pygame.draw.rect(screen, (40, 40, 50), rect, border_radius=10)

        info_text = self._get_info_text()

        y = rect.y + 10

        for line in info_text:
            text = self.small_font.render(line, True, (200, 200, 200))
            screen.blit(text, (20, y))
            y += 30

    def _get_info_text(self):
        return [
            "",
            "--- CARA BERMAIN ---",
            "• Gerakan: Gunakan Tombol ARROW atau WASD pada Keyboard",
            "• Pause    : Tekan ESC saat bermain",
            "• Restart   : Tekan R saat mode Pause atau Game Over",
            "",
            "--- ATURAN GAME ---",
            "• Makan kelinci untuk menambah skor dan panjang tubuh.",
            "• Game Over jika kepala menabrak tubuh sendiri.",
            "• Bisa menembus tembok",
            "",
            "--- INFORMASI LEVEL ---",
            "• EASY     : Gerakan lambat dan tetap.",
            "• MEDIUM : Kecepatan standar, bertambah jika score tinggi.",
            "• HARD     : Gerakan sangat cepat, akan semakin cepat lagi",
            "",
            "",
            "Design by: Fauzan Adhim Muntazhar (003) TIA25"
        ]

    # ==================== FULLSCREEN SYSTEM ====================
    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.calculate_layout()
        self.scroll_event()