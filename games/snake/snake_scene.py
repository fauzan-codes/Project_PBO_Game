# Project_PBO_Game\games\snake\snake_scene.py
import pygame

from games.snake.snake import Snake
from games.snake.food import Food
from games.snake.snake_renderer import SnakeRenderer
from games.snake.snake_ui import SnakeUI
from games.snake.snake_animation import SnakeAnimation

class SnakeScene:
    def __init__(self, width, height, game, assets):
        self.game = game
        self.width = width
        self.height = height
        self.assets = assets

        # objek
        self.renderer = SnakeRenderer(self.assets)
        self.ui = SnakeUI(width, height)
        self.anim = SnakeAnimation(width, height)

        # status
        self.state = "HOME"
        self.mouse_pos = None


        # score
        self.score = 0
        self.level = "easy"

        self.start_time = 0
        self.elapsed_time = 0
        self.pause_time = 0
        self.grid_count = 25

        self.music_started = False
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

        # escape
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:

                if self.state == "HOME":
                    pygame.mixer.music.stop()
                    from scenes.game_select import GameSelect
                    self.game.game_manager.change_scene(GameSelect(self.game.game_manager))

                elif self.state == "LEVEL":
                    self.state = "HOME"

                elif self.state == "PLAYING":
                    self.state = "PAUSE"
                    self.pause_start = pygame.time.get_ticks()
                    self.game.pause()

                elif self.state == "PAUSE":
                    self.state = "PLAYING"
                    self.pause_time += pygame.time.get_ticks() - self.pause_start
                    self.game.resume()
                return 


        if self.state == "HOME":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if mouse_pos:
                    self.state = "LEVEL"

        elif self.state == "LEVEL":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if mouse_pos:
                    if self.ui.easy.collidepoint(mouse_pos):
                        self.start_game("Easy")
                        self.state = "PLAYING"

                    elif self.ui.medium.collidepoint(mouse_pos):
                        self.start_game("Medium")
                        self.state = "PLAYING"

                    elif self.ui.hard.collidepoint(mouse_pos):
                        self.start_game("Hard")
                        self.state = "PLAYING"

        elif self.state == "PLAYING":
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

        elif self.state == "PAUSE":
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    self.start_game(self.level)
                    self.state = "PLAYING"

                elif event.key == pygame.K_h:
                    self.state = "HOME"

            # mouse
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.mouse_pos:
                    if self.ui.btn_resume.collidepoint(self.mouse_pos):
                        self.state = "PLAYING"
                        self.pause_time += pygame.time.get_ticks() - self.pause_start
                        self.game.resume()

                    elif self.ui.btn_restart.collidepoint(self.mouse_pos):
                        self.start_game(self.level)
                        self.state = "PLAYING"

                    elif self.ui.btn_home.collidepoint(self.mouse_pos):
                        self.state = "HOME"

        elif self.state == "GAME_OVER":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.start_game(self.level)
                    self.state = "PLAYING"
                elif event.key == pygame.K_h:
                    self.state = "HOME"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.mouse_pos:
                    if self.ui.btn_restart.collidepoint(self.mouse_pos):
                        self.start_game(self.level)
                        self.state = "PLAYING"

                    elif self.ui.btn_home.collidepoint(self.mouse_pos):
                        self.state = "HOME"
                

    def update(self):
        self.assets.update()
        current_time = pygame.time.get_ticks()

        # music delay
        if not self.music_started:
            if current_time - self.start_time >= 1500:
                self.game.game_manager.asset.play_music(self.assets.bgm_path, 0.3, -1)
                self.music_started = True

        if self.state == "PAUSE":
            self.game.game_manager.asset.set_volume(0.2)
            return

        if self.state == "GAME_OVER":
            self.game.game_manager.asset.set_volume(0.2)
            return

        if self.state in ["HOME", "LEVEL"]:
            self.anim.update()
            self.game.game_manager.asset.set_volume(0.3)
            return

        if self.state == "PLAYING":
            self.elapsed_time = (current_time - self.start_time - self.pause_time) // 1000
            self.game.game_manager.asset.set_volume(0.1)

            # makan
            if self.snake.body[0] == self.food.position:
                self.snake.eat()
                self.food.spawn(self.snake.body)
                self.assets.play_eat()
                self.score += 1

                if self.score % 3 == 0:
                    self.snake.increase_speed()

            # collision
            if self.snake.check_self_collision():
                self.assets.play_die()
                self.state = "GAME_OVER"
                self.game.pause()

                self.elapsed_time = (current_time - self.start_time - self.pause_time) // 1000

                self.snake = Snake(self.grid_count, self.grid_count, self.level)
                self.snake.move_timer = 0



    def draw(self, surface):
        if self.state == "PLAYING":
            self.renderer.draw_play(surface, self)

        elif self.state == "PAUSE":
            self.renderer.draw_play(surface, self)
            self.ui.draw_pause_menu(surface, self.mouse_pos)

        elif self.state == "GAME_OVER":
            self.renderer.draw_play(surface, self)
            self.ui.draw_game_over(surface, self.score, self.elapsed_time, self.mouse_pos)

        else:
            self.ui.draw_menu(surface, self)




        