import pygame
from games.snake.snake_assets import SnakeAssets
from games.snake.snake import Snake
from games.snake.food import Food
from games.snake.snake_renderer import SnakeRenderer
from games.snake.snake_ui import SnakeUI
from games.snake.snake_animation import SnakeAnimation

class SnakeScene:
    def __init__(self, width, height, game):
        self.game = game
        self.width = width
        self.height = height

        self.state = "home"
        self.mouse_pos = None

        self.assets = SnakeAssets()
        self.renderer = SnakeRenderer(self.assets)
        self.ui = SnakeUI(width, height)
        self.anim = SnakeAnimation(width, height)

        self.grid_count = 25

        self.score = 0
        self.level = "easy"

        self.start_time = 0
        self.elapsed_time = 0
        self.pause_time = 0

        self.start_game("easy")

    def start_game(self, level):
        self.start_time = pygame.time.get_ticks()
        self.elapsed_time = 0
        self.pause_time = 0

        self.level = level
        self.score = 0  
        self.snake = Snake(self.grid_count, self.grid_count, level)
        self.food = Food(self.grid_count, self.grid_count)

        self.snake.move_timer = 0

        self.game.objects.clear()
        self.game.objects += [self.snake, self.food]

        self.food.spawn(self.snake.body)
        self.game.resume()




    def handle_event(self, event, mouse_pos):
        self.mouse_pos = mouse_pos

        # ================= GLOBAL ESC =================
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:

                if self.state == "home":
                    from scenes.game_select import GameSelect
                    self.game.game_manager.change_scene(GameSelect(self.game.game_manager))

                elif self.state == "level":
                    self.state = "home"

                elif self.state == "play":
                    self.state = "pause"
                    self.pause_start = pygame.time.get_ticks()

                    # self.snake.move_timer = 0
                    self.game.pause()

                elif self.state == "pause":
                    self.state = "play"
                    self.pause_time += pygame.time.get_ticks() - self.pause_start

                    # self.snake.move_timer = 0
                    self.game.resume()

                return 

        # ================= HOME =================
        if self.state == "home":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.state = "level"

        # ================= LEVEL =================
        elif self.state == "level":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if mouse_pos:
                    if self.ui.easy.collidepoint(mouse_pos):
                        self.start_game("easy")
                        self.state = "play"

                    elif self.ui.medium.collidepoint(mouse_pos):
                        self.start_game("medium")
                        self.state = "play"

                    elif self.ui.hard.collidepoint(mouse_pos):
                        self.start_game("hard")
                        self.state = "play"

        # ================= PLAY =================
        elif self.state == "play":
            if event.type == pygame.KEYDOWN:

                dirs = {
                    pygame.K_w:(0,-1),
                    pygame.K_s:(0,1),
                    pygame.K_a:(-1,0),
                    pygame.K_d:(1,0),
                    pygame.K_UP:(0,-1),
                    pygame.K_DOWN:(0,1),
                    pygame.K_LEFT:(-1,0),
                    pygame.K_RIGHT:(1,0),
                }

                if event.key in dirs:
                    self.snake.set_direction(dirs[event.key])

        # ================= PAUSE =================
        elif self.state == "pause":
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    self.start_game(self.level)
                    self.state = "play"

                elif event.key == pygame.K_h:
                    self.state = "home"

            # mouse button pause
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.mouse_pos:
                    if self.ui.btn_resume.collidepoint(self.mouse_pos):
                        self.state = "play"

                    elif self.ui.btn_restart.collidepoint(self.mouse_pos):
                        self.start_game(self.level)
                        self.state = "play"

                    elif self.ui.btn_home.collidepoint(self.mouse_pos):
                        self.state = "home"

        elif self.state == "game_over":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.start_game(self.level)
                    self.state = "play"
                elif event.key == pygame.K_h:
                    self.state = "home"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.mouse_pos:
                    if self.ui.btn_restart.collidepoint(self.mouse_pos):
                        self.start_game(self.level)
                        self.state = "play"

                    elif self.ui.btn_home.collidepoint(self.mouse_pos):
                        self.state = "home"
                

    def update(self):
        self.assets.update()

        # ================= PLAY =================
        if self.state == "play":
            current_time = pygame.time.get_ticks()
            self.elapsed_time = (current_time - self.start_time - self.pause_time) // 1000

            # makan
            if self.snake.body[0] == self.food.position:
                self.snake.eat()
                self.food.spawn(self.snake.body)
                self.score += 1

                if self.score % 3 == 0:
                    self.snake.increase_speed()

            # mati
            if self.snake.check_self_collision():
                self.state = "game_over"
                self.game.pause()

                # freeze time
                current_time = pygame.time.get_ticks()
                self.elapsed_time = (current_time - self.start_time - self.pause_time) // 1000
                self.snake = Snake(self.grid_count, self.grid_count, self.level)
                self.snake.move_timer = 0

        elif self.state in ["home", "level"]:
            self.anim.update()

        elif self.state in ["pause", "game_over"]:
            return



    def draw(self, surface):
        if self.state == "play":
            self.draw_play(surface)

        elif self.state == "pause":
            self.draw_play(surface)
            self.ui.draw_pause_menu(surface, self.mouse_pos)

        elif self.state == "game_over":
            self.draw_play(surface)
            self.ui.draw_game_over(surface, self.score, self.elapsed_time, self.mouse_pos)

        else:
            self.draw_menu(surface)



    def draw_menu(self, surface):
        bg = self.assets.get_bg()

        # background
        for y in range(0, self.height, 16):
            for x in range(0, self.width, 16):
                surface.blit(bg, (x, y))

        # animasi snake
        self.renderer.draw(surface, self.anim.body, 16)

        # ===== HOME UI =====
        if self.state == "home":
            title = self.ui.font_big.render("SNAKE", True, (255,255,0))
            surface.blit(title, (self.width//2 - title.get_width()//2, 80))

            text = self.ui.font.render("CLICK TO START", True, (255,255,255))
            surface.blit(text, (self.width//2 - text.get_width()//2, self.height - 100))

        # ===== LEVEL UI =====
        elif self.state == "level":
            title = self.ui.font_big.render("SELECT LEVEL", True, (255,255,0))
            surface.blit(title, (self.width//2 - title.get_width()//2, 100))

            self.ui.draw_button(surface, self.ui.easy, "EASY", self.mouse_pos)
            self.ui.draw_button(surface, self.ui.medium, "MEDIUM", self.mouse_pos)
            self.ui.draw_button(surface, self.ui.hard, "HARD", self.mouse_pos)

    def draw_play(self, surface):
        surface.fill((20, 20, 30))

        # ===== LAYOUT =====
        sidebar_width = 200
        padding = 20

        map_area_width = self.width - sidebar_width - padding*3
        map_area_height = self.height - padding*2

        map_size = min(map_area_width, map_area_height)

        tile = map_size // self.grid_count

        map_size = tile * self.grid_count

        offset_x = padding
        offset_y = (self.height - map_size) // 2

        # ===== DRAW BORDER MAP =====
        border_rect = pygame.Rect(
            offset_x - 4,
            offset_y - 4,
            map_size + 8,
            map_size + 8
        )

        pygame.draw.rect(surface, (100, 255, 100), border_rect, border_radius=8)

        # ===== DRAW MAP =====
        bg = pygame.transform.scale(self.assets.get_bg(), (tile, tile))

        for y in range(self.grid_count):
            for x in range(self.grid_count):
                surface.blit(bg, (offset_x + x*tile, offset_y + y*tile))

        # ===== DRAW FOOD =====
        fx, fy = self.food.position
        food_img = pygame.transform.scale(self.assets.get_food(), (tile, tile))
        surface.blit(food_img, (offset_x + fx*tile, offset_y + fy*tile))

        # ===== DRAW SNAKE =====
        self.renderer.draw(surface, self.snake.body, tile, (offset_x, offset_y))

        # ===== SIDEBAR =====
        panel_x = offset_x + map_size + padding
        panel_y = offset_y
        panel_width = sidebar_width
        panel_height = map_size

        self.ui.draw_side_panel(
            surface,
            panel_x,
            panel_y,
            panel_width,
            panel_height,
            self.score,
            self.level,
            self.elapsed_time
        )

        