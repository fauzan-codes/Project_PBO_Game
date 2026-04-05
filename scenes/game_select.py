# .\scene\game_select.py
import pygame
from games.snake.snake_game import SnakeGame
from games.flappy_bird.flappy_game import FlappyGame
from games.dino_run.dino_game import DinoGame

class GameSelect:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 60)

        self.games = [
            {
                "name": "Classic Snake",
                "class": SnakeGame,
                "image": "Snake_poster.png"
            },
            {
                "name": "Flappy Bird", 
                "class": FlappyGame, 
                "image": "flappyBird-poster.png"
            },
            {
                "name": "Dino Run Chrome", 
                "class": DinoGame, 
                "image": "Snake_poster.png"
            },
            {
                "name": "Game 4", 
                "class": None, 
                "image": "img-tes.png"
            },
            {
                "name": "Game 5", 
                "class": None, 
                "image": "img-tes.png"
            },
        ]


        # load img
        self.loaded_images = []
        for game in self.games:
            if game["image"]:
                img = self.game_manager.asset.load_image(game["image"])
                self.loaded_images.append(img)
            else:
                self.loaded_images.append(None)


        self.selected = 0
        self.card_rects = []

        self.game_manager.asset.play_random_music(volume=0.3)


    # ===== HANDLE EVENT =====
    def handle_event(self, event):
        # KEYBOARD
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.selected = (self.selected + 1) % len(self.games)
            elif event.key == pygame.K_LEFT:
                self.selected = (self.selected - 1) % len(self.games)

            elif event.key == pygame.K_RETURN:
                self.start_game(self.selected)

            elif event.key == pygame.K_ESCAPE:
                from scenes.home import Home
                self.game_manager.change_scene(Home(self.game_manager))

        # MOUSE
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            # BACK BUTTON
            for i, rect in enumerate(self.card_rects):
                if rect.collidepoint(mouse_pos):
                    self.start_game(i)

            if self.back_rect.collidepoint(mouse_pos):
                from scenes.home import Home
                self.game_manager.change_scene(Home(self.game_manager))



    def start_game(self, index):
        game_class = self.games[index]["class"]
        if game_class:
            # self.game_manager.asset.fade_out_music(500) #stop music
            game = game_class(self.game_manager)
            self.game_manager.change_scene(game, fade_music=True)

    def update(self):
        self.game_manager.asset.update_music()


    # ===== UI =====
    def draw(self, screen):
        screen.fill((30, 30, 40))

        screen_width = screen.get_width()

    
        # title
        title = self.title_font.render("SELECT GAME", True, (255, 255, 255))
        title_rect = title.get_rect(center=(screen_width // 2, 80))
        screen.blit(title, title_rect)

        mouse_pos = pygame.mouse.get_pos()

        cols = 3
        card_width = 200
        card_height = 230

        image_height = 150
        padding = 30

        total_width = cols * card_width + (cols - 1) * padding
        start_x = (screen_width - total_width) // 2
        start_y = 150

        self.card_rects = []


        # card
        for i, game in enumerate(self.games):
            row = i // cols
            col = i % cols

            x = start_x + col * (card_width + padding)
            y = start_y + row * (card_height + padding)

            rect = pygame.Rect(x, y, card_width, card_height)
            self.card_rects.append(rect)

            if rect.collidepoint(mouse_pos):
                self.selected = i

            # hover effect
            color = (200, 200, 200) # Mouse hover
            if rect.collidepoint(mouse_pos):
                color = (255, 255, 0)
            elif i == self.selected: # Keyboard hover
                color = (255, 255, 0)

            shadow = rect.copy()
            shadow.y += 5
            pygame.draw.rect(screen, (50, 50, 50), shadow, border_radius=15)
            pygame.draw.rect(screen, color, rect, border_radius=15)

     
            # img
            image_rect = pygame.Rect(x, y, card_width, image_height)
            img = self.loaded_images[i]

            if img:
                img_width, img_height = img.get_size()

                target_ratio = 4 / 3 # rasio 4:3
                current_ratio = img_width / img_height

                if current_ratio > target_ratio:
                    new_width = int(img_height * target_ratio)
                    crop_x = (img_width - new_width) // 2
                    img_cropped = img.subsurface((crop_x, 0, new_width, img_height))
                else:
                    new_height = int(img_width / target_ratio)
                    crop_y = (img_height - new_height) // 2
                    img_cropped = img.subsurface((0, crop_y, img_width, new_height))

                img_scaled = pygame.transform.smoothscale(img_cropped, (card_width, image_height))
                img_scaled = pygame.transform.smoothscale(img_cropped, (card_width, image_height))

                mask_surface = pygame.Surface((card_width, image_height), pygame.SRCALPHA)

                pygame.draw.rect(
                    mask_surface,
                    (255, 255, 255),
                    mask_surface.get_rect(),
                    border_top_left_radius=15,
                    border_top_right_radius=15
                )

                final_image = pygame.Surface((card_width, image_height), pygame.SRCALPHA)
                final_image.blit(img_scaled, (0, 0))
                final_image.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

                screen.blit(final_image, (x, y))
            else:
                pygame.draw.rect(screen, (100, 100, 120), image_rect)

     

            # title area
            title_area = pygame.Rect(x, y + image_height, card_width, card_height - image_height)
            words = game["name"].split(" ")
            line1 = ""
            line2 = ""

            if len(words) > 1:
                mid = len(words) // 2
                line1 = " ".join(words[:mid])
                line2 = " ".join(words[mid:])
            else:
                line1 = game["name"]

            text1 = self.font.render(line1, True, (0, 0, 0))
            text1_rect = text1.get_rect(center=(title_area.centerx, title_area.y + 25))
            screen.blit(text1, text1_rect)

            if line2:
                text2 = self.font.render(line2, True, (0, 0, 0))
                text2_rect = text2.get_rect(center=(title_area.centerx, title_area.y + 55))
                screen.blit(text2, text2_rect)

            if i == self.selected:
                pygame.draw.rect(screen, (255, 255, 0), rect, 4, border_radius=15)

        # back button
        self.back_rect = pygame.Rect(30, screen.get_height() - 70, 120, 40)
        back_color = (255, 255, 0) if self.back_rect.collidepoint(mouse_pos) else (200, 200, 200)
        pygame.draw.rect(screen, back_color, self.back_rect, border_radius=10)
        back_text = self.font.render("BACK", True, (0, 0, 0))
        back_text_rect = back_text.get_rect(center=self.back_rect.center)
        screen.blit(back_text, back_text_rect)