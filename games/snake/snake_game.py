import pygame
from core.base_game import BaseGame
# from scenes.game_select import GameSelect

class SnakeGame(BaseGame):
    def __init__(self, game_manager):
        self.game_manager = game_manager

        # ===== STATE =====
        self.state = "home"  # home | play | game_over

        # ===== SCREEN =====
        self.screen = pygame.display.get_surface()
        self.width, self.height = self.screen.get_size()

        # ===== UI AREA =====
        self.header_height = 60
        self.info_height = 120

        # game window (default size)
        self.game_width = 400
        self.game_height = 400

        self.fullscreen = False

        self._calculate_layout()

        # ===== FONT =====
        self.font = pygame.font.Font(None, 40)
        self.small_font = pygame.font.Font(None, 28)

        # ===== SCROLL INFO =====
        self.info_scroll = 0
        self.scroll_y = 0

        # nanti diisi
        self.home = None

    # =========================
    # 📐 Layout System
    # =========================
    def _calculate_layout(self):
        if self.fullscreen:
            self.game_rect = pygame.Rect(0, 0, self.width, self.height)
        else:
            # center game window
            x = (self.width - self.game_width) // 2
            y = self.header_height + 20

            self.game_rect = pygame.Rect(x, y, self.game_width, self.game_height)

        # header
        self.header_rect = pygame.Rect(0, 0, self.width, self.header_height)

        # info panel
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

    # =========================
    # 🎮 EVENT
    # =========================
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                from scenes.game_select import GameSelect
                self.game_manager.change_scene(GameSelect(self.game_manager))

            if event.key == pygame.K_f:
                self.toggle_fullscreen()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # scroll up
                self.scroll_y += 20
            elif event.button == 5:  # scroll down
                self.scroll_y -= 20
        
        self._clamp_scroll()

    # =========================
    # 🔄 UPDATE
    # =========================
    def update(self):
        pass

    def _get_content_height(self):
        if self.fullscreen:
            return self.height

        # hitung tinggi teks info
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
    
    def _clamp_scroll(self):
        content_height = self._get_content_height()

        min_scroll = min(0, self.height - content_height)
        max_scroll = 0

        if self.scroll_y < min_scroll:
            self.scroll_y = min_scroll
        if self.scroll_y > max_scroll:
            self.scroll_y = max_scroll

    # =========================
    # 🎨 DRAW
    # =========================
    def draw(self, screen):
        screen.fill((30, 30, 30))

        # game & info dulu (yang kena scroll)
        self._draw_game_area(screen)
        if not self.fullscreen:
            self._draw_info(screen)

        self._draw_header(screen)

    # =========================
    # 🔝 HEADER
    # =========================
    def _draw_header(self, screen):
        pygame.draw.rect(screen, (50, 50, 50), self.header_rect)

        # ===== BACK BUTTON =====
        back_text = self.small_font.render("< Back", True, (255, 255, 255))
        screen.blit(back_text, (10, 15))

        # ===== TITLE =====
        title = self.font.render("SNAKE GAME", True, (255, 255, 255))
        screen.blit(title, (self.width // 2 - title.get_width() // 2, 15))

        # ===== FULLSCREEN BUTTON =====
        text = "Windowed" if self.fullscreen else "Fullscreen"

        self.fullscreen_rect = pygame.Rect(
            self.width - 150, 10, 140, 40
        )

        mouse_pos = pygame.mouse.get_pos()

        color = (200, 200, 200)
        if self.fullscreen_rect.collidepoint(mouse_pos):
            color = (255, 255, 0)

        pygame.draw.rect(screen, color, self.fullscreen_rect, border_radius=8)

        btn_text = self.small_font.render(text, True, (0, 0, 0))
        text_rect = btn_text.get_rect(center=self.fullscreen_rect.center)
        screen.blit(btn_text, text_rect)

    # =========================
    # 🎮 GAME WINDOW
    # =========================
    def _draw_game_area(self, screen):
        rect = self.game_rect.copy()
        rect.y += self.scroll_y

        pygame.draw.rect(screen, (0, 0, 0), rect)

        text = self.small_font.render("GAME AREA", True, (255, 255, 255))
        screen.blit(
            text,
            (
                rect.centerx - text.get_width() // 2,
                rect.centery
            )
        )

    # =========================
    # 📜 INFO PANEL
    # =========================
    def _draw_info(self, screen):
        rect = self.info_rect.copy()
        rect.y += self.scroll_y

        pygame.draw.rect(screen, (40, 40, 40), rect)

        info_text = self._get_info_text()

        y = rect.y + 10

        for line in info_text:
            text = self.small_font.render(line, True, (200, 200, 200))
            screen.blit(text, (20, y))
            y += 30

    def _get_info_text(self):
        return [
            "Snake Game",
            "",
            "- Gunakan WASD / Arrow",
            "- Makan makanan untuk score",
            "- Jangan makan diri sendiri",
            "- Tembus tembok",
            "",
            "Press F untuk fullscreen",
            "Press F untuk fullscreen",
            "Press F untuk fullscreen",
            "Press F untuk fullscreen",
            "Press F untuk fullscreen",
            "Press F untuk fullscreen",
            "Press F untuk fullscreen",
            "Press F untuk fullscreen",
            "Press F untuk fullscreen",
            "Press F untuk fullscreen",
            "Press F untuk fullscreen"
        ]

    # =========================
    # 🖥️ FULLSCREEN
    # =========================
    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self._calculate_layout()
        self._clamp_scroll()