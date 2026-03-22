import pygame
from games.snake.snake_assets import SnakeAssets
from games.snake.snake import Snake
from games.snake.food import Food

class SnakeScene:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.state = "home"  # home | level | play | pause

        self.font_big = pygame.font.Font(None, 80)
        self.font = pygame.font.Font(None, 40)

        # tombol
        self.play_rect = pygame.Rect(0, 0, 200, 60)
        self.play_rect.center = (width // 2, height // 2 + 50)

        # tombol easy
        self.easy_rect = pygame.Rect(0, 0, 200, 60)
        self.easy_rect.center = (self.width // 2, self.height // 2)

        self.mouse_pos = None
        self.assets = SnakeAssets()

        # animasi sederhana (nanti pakai snake_assets)
        self.anim_y = height // 2 - 100
        self.anim_x = 0

        self.grid_count = 25   # jumlah tile (FIX)

        # hitung ukuran tile biar muat tinggi
        self.grid_size = self.height // self.grid_count

        self.grid_width = self.grid_count
        self.grid_height = self.grid_count

        self.snake = Snake(self.grid_count, self.grid_count)
        self.food = Food(self.grid_count, self.grid_count)
        self.food.spawn(self.snake.body)
        self.score = 0

    # ================= EVENT =================
    def handle_event(self, event, mouse_pos):
        self.mouse_pos = mouse_pos
        if self.state == "home":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos and self.play_rect.collidepoint(mouse_pos):
                    self.state = "level"

        if self.state == "level":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos and self.easy_rect.collidepoint(mouse_pos):
                    self.start_game("easy")

        if self.state == "play":
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_w, pygame.K_UP]:
                    self.snake.set_direction((0, -1))
                elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                    self.snake.set_direction((1, 0))
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    self.snake.set_direction((0, 1))
                elif event.key in [pygame.K_a, pygame.K_LEFT]:
                    self.snake.set_direction((-1, 0))

    # ================= UPDATE =================
    def update(self):
        self.assets.update()
        if self.state == "home":
            self.anim_x += 2
            if self.anim_x > self.width:
                self.anim_x = -100

        if self.state == "play":
            self.snake.update()

            # makan food
            if self.snake.body[0] == self.food.position:
                self.snake.eat()
                self.food.spawn(self.snake.body)
                self.score += 1

            # mati
            if self.snake.check_self_collision():
                self.state = "game_over"

    # ================= DRAW =================
    def draw(self, surface):
        if self.state == "home":
            self.draw_home(surface)

        elif self.state == "level":
            self.draw_level(surface)

        elif self.state == "play":
            self.draw_play(surface)

    # ================= HOME =================
    def draw_home(self, surface):
        bg = self.assets.get_bg()

        for y in range(0, self.height, 16):
            for x in range(0, self.width, 16):
                surface.blit(bg, (x, y))

        # judul
        title = self.font_big.render("SNAKE", True, (255, 255, 0))
        surface.blit(title, (self.width//2 - title.get_width()//2, 80))

        # animasi snake (sementara kotak dulu)
        tiles = self.assets.get_tiles()

        # arah ke kanan
        head = self.assets.get_head(1)   # kanan
        body = tiles[13]                # horizontal
        tail = self.assets.get_tail(1)

        # gambar snake (5 segment)
        for i in range(5):
            x = self.anim_x - i * 16
            y = self.anim_y

            if i == 0:
                sprite = head
            elif i == 4:
                sprite = tail
            else:
                sprite = body

            surface.blit(sprite, (x, y))

        # tombol PLAY
        self.draw_button(surface, self.play_rect, "PLAY")

    def draw_button(self, surface, rect, text):
        mouse_pos = self.mouse_pos

        color = (200, 200, 200)
        if mouse_pos and rect.collidepoint(mouse_pos):
            color = (255, 255, 0)

        pygame.draw.rect(surface, color, rect, border_radius=10)

        txt = self.font.render(text, True, (0, 0, 0))
        surface.blit(txt, txt.get_rect(center=rect.center))

    def draw_play(self, surface):
        tile = self.grid_size

        # background luar
        surface.fill((30, 30, 40))

        # center map
        map_size = tile * self.grid_count
        offset_x = (self.width - map_size) // 2
        offset_y = (self.height - map_size) // 2

        # ===== SCALE ASSETS =====
        bg = pygame.transform.scale(self.assets.get_bg(), (tile, tile))
        food_img = pygame.transform.scale(self.assets.get_food(), (tile, tile))

        # map
        for y in range(self.grid_count):
            for x in range(self.grid_count):
                surface.blit(bg, (offset_x + x*tile, offset_y + y*tile))

        # food
        fx, fy = self.food.position
        surface.blit(food_img, (offset_x + fx*tile, offset_y + fy*tile))


        # snake
        tiles = self.assets.get_tiles()
        tile = self.grid_size

        for i in range(len(self.snake.body)):
            x, y = self.snake.body[i]
            pos = (offset_x + x*tile, offset_y + y*tile)

            # HEAD
            if i == 0:
                dir = self.get_dir(self.snake.body[i], self.snake.body[i+1])

                direction_map = {
                    (0, -1): 2,
                    (1, 0): 3,
                    (0, 1): 0,
                    (-1, 0): 1
                }

                sprite = self.assets.get_head(direction_map[dir])

            # TAIL
            elif i == len(self.snake.body) - 1:
                dir = self.get_dir(self.snake.body[i-1], self.snake.body[i])

                direction_map = {
                    (0, -1): 2,
                    (1, 0): 3,
                    (0, 1): 0,
                    (-1, 0): 1
                }

                sprite = self.assets.get_tail(direction_map[dir])

            # BODY
            else:
                prev_dir = self.get_dir(self.snake.body[i-1], self.snake.body[i])
                next_dir = self.get_dir(self.snake.body[i], self.snake.body[i+1])

                if prev_dir == next_dir:
                    sprite = self.assets.get_body_straight(prev_dir)
                else:
                    sprite = self.assets.get_turn(prev_dir, next_dir)

            # SCALE
            sprite = pygame.transform.scale(sprite, (tile, tile))
            surface.blit(sprite, pos)

    def draw_level(self, surface):
        surface.fill((20, 20, 30))

        title = self.font_big.render("SELECT LEVEL", True, (255, 255, 0))
        surface.blit(title, (self.width//2 - title.get_width()//2, 100))

        self.draw_button(surface, self.easy_rect, "EASY")

    def start_game(self, level):
        self.state = "play"

        # reset snake & food
        self.snake = Snake(self.grid_count, self.grid_count)
        self.food = Food(self.grid_count, self.grid_count)
        self.food.spawn(self.snake.body)

        self.score = 0

        # speed
        if level == "easy":
            self.snake.move_delay = 12


    def get_dir(self, a, b):
        dx = b[0] - a[0]
        dy = b[1] - a[1]

        if dx != 0:
            dx = dx // abs(dx)
        if dy != 0:
            dy = dy // abs(dy)

        return (dx, dy)