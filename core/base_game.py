# Project_PBO_Game\core\base_game.py
import pygame

class BaseGame:
    def __init__(self):
        self.is_running = True
        self.is_paused = False
        self.objects = []

        self.game_manager = None

        # screen
        self.screen = pygame.display.get_surface()
        self.width, self.height = self.screen.get_size()

        # UI
        self.header_height = 60
        self.game_width = 800
        self.game_height = 600

        self.game_surface = pygame.Surface((self.game_width, self.game_height))
        self.fullscreen = False

        self.scroll_y = 0

        self.font = pygame.font.Font(None, 40)
        self.small_font = pygame.font.Font(None, 28)

        self.graph = False
        self.calculate_layout()

    # ==================== OVERRIDE AREA ====================
    def get_title(self):
        return "GAME"

    def get_info_text(self):
        return ["No info"]

    def get_scene(self):
        return None

    # ==================== LAYOUT ====================
    def calculate_layout(self):
        ratio = 4 / 3

        if self.fullscreen:
            available_width = self.width
            available_height = self.height - self.header_height

            new_height = available_height
            new_width = int(new_height * ratio)

            if new_width > available_width:
                new_width = available_width
                new_height = int(new_width / ratio)

            x = (self.width - new_width) // 2
            y = self.header_height + (available_height - new_height) // 2

            self.game_rect = pygame.Rect(x, y, new_width, new_height)
        else:
            x = (self.width - self.game_width) // 2
            y = self.header_height + 20
            self.game_rect = pygame.Rect(x, y, self.game_width, self.game_height)

        self.header_rect = pygame.Rect(0, 0, self.width, self.header_height)

        if not self.fullscreen:
            margin_x = 60
            info_width = self.width - (margin_x * 2)
            info_height = len(self.get_info_text()) * 30 + 20
            info_x = (self.width - info_width) // 2

            self.info_rect = pygame.Rect(info_x, self.game_rect.bottom + 10,self.width - (margin_x*2),info_height)
        else:
            self.info_rect = None

    # ==================== EVENT ====================
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                self.toggle_fullscreen()
            if event.key == pygame.K_m:
                self.game_manager.asset.toggle_mute()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if hasattr(self, "back_rect") and self.back_rect.collidepoint(mouse_pos):
                pygame.mixer.music.stop()
                from scenes.game_select import GameSelect
                self.game_manager.change_scene(GameSelect(self.game_manager))

            if hasattr(self, "fullscreen_rect") and self.fullscreen_rect.collidepoint(mouse_pos):
                self.toggle_fullscreen()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.scroll_y += 20
            elif event.button == 5:
                self.scroll_y -= 20

            self.scroll_event()

        # kirim event ke scene
        if hasattr(self, "scene") and self.scene:
            mx, my = pygame.mouse.get_pos()
            inner_rect = self.game_rect.inflate(-10, -10)
            inner_rect.y += self.scroll_y

            rel_mouse = None

            if inner_rect.collidepoint(mx, my):
                rel_x = (mx - inner_rect.x) * (self.game_width / inner_rect.width)
                rel_y = (my - inner_rect.y) * (self.game_height / inner_rect.height)
                rel_mouse = (rel_x, rel_y)

            self.scene.handle_event(event, rel_mouse)

    # ==================== UPDATE ====================
    def update(self):
        current_surface = pygame.display.get_surface()
        new_width, new_height = current_surface.get_size()

        if new_width != self.width or new_height != self.height:
            self.update_screen_size()


        if not self.is_paused:
            for obj in self.objects:
                obj.update()

        if hasattr(self, "scene") and self.scene:
            self.scene.update()

    # ==================== DRAW ====================
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

        pygame.draw.rect(screen, (200, 200, 200), rect, border_radius=5)
        inner_rect = rect.inflate(-10, -10)

        self.game_surface.fill((0, 0, 0))

        if hasattr(self, "scene") and self.scene:
            self.scene.draw(self.game_surface)


        if self.graph: #smooth grafik
            scaled = pygame.transform.smoothscale(
                self.game_surface,
                (inner_rect.width, inner_rect.height)
            )
        else: #gameplay
            scaled = pygame.transform.scale(
                self.game_surface,
                (inner_rect.width, inner_rect.height)
            )

        screen.blit(scaled, (inner_rect.x, inner_rect.y))

    # ==================== HEADER ====================
    def draw_header(self, screen):
        shadow = self.header_rect.copy()
        shadow.y += 1
        pygame.draw.rect(screen, (50, 50, 50), shadow)
        pygame.draw.rect(screen, (40, 40, 60), self.header_rect)

        title = self.font.render(self.get_title(), True, (255, 255, 255))
        screen.blit(title, (self.width // 2 - title.get_width() // 2, 15))

        self.back_rect = pygame.Rect(20, 10, 100, 40)
        self.draw_button(screen, self.back_rect, "BACK")

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

        pygame.draw.rect(screen, color, rect, border_radius=10)

        txt = self.small_font.render(text, True, (0, 0, 0))
        screen.blit(txt, txt.get_rect(center=rect.center))

    # ==================== INFO ====================
    def draw_info(self, screen):
        rect = self.info_rect.copy()
        rect.y += self.scroll_y

        shadow = rect.copy()
        shadow.y += 5
        pygame.draw.rect(screen, (50, 50, 50), shadow, border_radius=10)
        pygame.draw.rect(screen, (40, 40, 50), rect, border_radius=10)

        y = rect.y + 10

        for line in self.get_info_text():
            text = self.small_font.render(line, True, (200, 200, 200))
            screen.blit(text, (rect.x + 20, y))
            y += 30

    # ==================== SCROLL ====================
    def get_content_height(self):
        if self.fullscreen:
            return self.height

        info_height = len(self.get_info_text()) * 30 + 20

        return (
            self.header_height +
            20 +
            self.game_height +
            10 +
            info_height
        )

    def scroll_event(self):
        content_height = self.get_content_height()

        min_scroll = min(0, self.height - content_height)

        if self.scroll_y < min_scroll:
            self.scroll_y = min_scroll
        if self.scroll_y > 0:
            self.scroll_y = 0

    # ==================== CONTROL ====================
    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.calculate_layout()
        self.scroll_event()


    def update_screen_size(self):
        self.screen = pygame.display.get_surface()
        self.width, self.height = self.screen.get_size()

        self.scroll_y = 0

        self.calculate_layout()
        self.scroll_event()


    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

    def restart(self):
        self.objects.clear()

    def exit(self):
        self.is_running = False