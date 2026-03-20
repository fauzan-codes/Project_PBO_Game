import pygame

class Home:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.Font(None, 60)
        self.small_font = pygame.font.Font(None, 40)

        self.selected = 0  # 0 = play, 1 = quit

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % 2
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % 2

            elif event.key == pygame.K_RETURN:
                if self.selected == 0:
                    from scenes.game_select import GameSelect
                    self.game_manager.current_scene = GameSelect(self.game_manager)
                elif self.selected == 1:
                    pygame.quit()
                    print("GAME KELUAR")
                    exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if self.play_rect.collidepoint(mouse_pos):
                from scenes.game_select import GameSelect
                self.game_manager.current_scene = GameSelect(self.game_manager)

            elif self.quit_rect.collidepoint(mouse_pos):
                pygame.quit()
                print("GAME KELUAR")
                exit()

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((20, 20, 30))

        screen_width = screen.get_width()
        screen_height = screen.get_height()

        title = self.font.render("GAME COLLECTION", True, (255, 255, 255))
        title_rect = title.get_rect(center=(screen_width // 2, 150))
        screen.blit(title, title_rect)

        mouse_pos = pygame.mouse.get_pos()

        # ===== PLAY BUTTON =====
        self.play_rect = pygame.Rect(0, 0, 250, 60)
        self.play_rect.center = (screen_width // 2, screen_height // 2)

        # sync mouse -> selected
        if self.play_rect.collidepoint(mouse_pos):
            self.selected = 0

        color_play = (200, 200, 200)
        if self.play_rect.collidepoint(mouse_pos) or self.selected == 0:
            color_play = (255, 255, 0)

        # shadow
        shadow = self.play_rect.copy()
        shadow.y += 5
        pygame.draw.rect(screen, (50, 50, 50), shadow, border_radius=15)

        pygame.draw.rect(screen, color_play, self.play_rect, border_radius=15)

        play_text = self.small_font.render("PLAY", True, (0, 0, 0))
        play_text_rect = play_text.get_rect(center=self.play_rect.center)
        screen.blit(play_text, play_text_rect)

        # ===== QUIT BUTTON =====
        self.quit_rect = pygame.Rect(0, 0, 250, 60)
        self.quit_rect.center = (screen_width // 2, screen_height // 2 + 90)

        # sync mouse -> selected
        if self.quit_rect.collidepoint(mouse_pos):
            self.selected = 1

        color_quit = (200, 200, 200)
        if self.quit_rect.collidepoint(mouse_pos) or self.selected == 1:
            color_quit = (255, 255, 0)

        # shadow
        shadow = self.quit_rect.copy()
        shadow.y += 5
        pygame.draw.rect(screen, (50, 50, 50), shadow, border_radius=15)

        pygame.draw.rect(screen, color_quit, self.quit_rect, border_radius=15)

        quit_text = self.small_font.render("QUIT", True, (0, 0, 0))
        quit_text_rect = quit_text.get_rect(center=self.quit_rect.center)
        screen.blit(quit_text, quit_text_rect)