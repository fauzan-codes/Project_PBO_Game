# Project_PBO_Game\games\snake\snake_renderer.py
import pygame

class SnakeRenderer:
    def __init__(self, assets):
        self.assets = assets

    def draw(self, surface, snake_body, tile, offset=(0,0)):
        offset_x, offset_y = offset

        for i in range(len(snake_body)):
            x, y = snake_body[i]
            pos = (offset_x + x * tile, offset_y + y * tile)

            if i == 0:
                dir = self.get_dir(snake_body[i], snake_body[i+1])
                sprite = self.assets.get_head(self.dir_to_index(dir))

            elif i == len(snake_body) - 1:
                dir = self.get_dir(snake_body[i-1], snake_body[i])
                sprite = self.assets.get_tail(self.dir_to_index(dir))

            else:
                prev_dir = self.get_dir(snake_body[i-1], snake_body[i])
                next_dir = self.get_dir(snake_body[i], snake_body[i+1])

                if prev_dir == next_dir:
                    sprite = self.assets.get_body_straight(prev_dir)
                else:
                    sprite = self.assets.get_turn(prev_dir, next_dir)

            sprite = pygame.transform.scale(sprite, (tile, tile))
            surface.blit(sprite, pos)

    def dir_to_index(self, dir):
        return {
            (0, -1): 2,
            (1, 0): 3,
            (0, 1): 0,
            (-1, 0): 1
        }[dir]

    def get_dir(self, a, b):
        dx = b[0] - a[0]
        dy = b[1] - a[1]

        if abs(dx) > 1:
            dx = -1 if dx > 0 else 1
        if abs(dy) > 1:
            dy = -1 if dy > 0 else 1

        return (dx, dy)
    
    def draw_border(self, surface, rect):
        pygame.draw.rect(surface, (200,200,200), rect, 4, border_radius=10)


    def draw_play(self, surface, scene):
        surface.fill((20, 20, 30))

        width = scene.width
        height = scene.height
        grid_count = scene.grid_count

        sidebar_width = 200
        padding = 20

        map_area_width = width - sidebar_width - padding*3
        map_area_height = height - padding*2

        map_size = min(map_area_width, map_area_height)

        tile = map_size // grid_count
        map_size = tile * grid_count

        offset_x = padding
        offset_y = (height - map_size) // 2

        # border
        border_rect = pygame.Rect(
            offset_x - 4,
            offset_y - 4,
            map_size + 8,
            map_size + 8
        )
        pygame.draw.rect(surface, (100, 255, 100), border_rect, border_radius=8)

        # map
        bg = pygame.transform.scale(scene.assets.get_bg(), (tile, tile))
        for y in range(grid_count):
            for x in range(grid_count):
                surface.blit(bg, (offset_x + x*tile, offset_y + y*tile))

        # food
        fx, fy = scene.food.position
        food_img = pygame.transform.scale(scene.assets.get_food(), (tile, tile))
        surface.blit(food_img, (offset_x + fx*tile, offset_y + fy*tile))

        # snake
        self.draw(surface, scene.snake.body, tile, (offset_x, offset_y))

        # side panel
        panel_x = offset_x + map_size + padding
        panel_y = offset_y

        scene.ui.draw_side_panel(
            surface,
            panel_x,
            panel_y,
            sidebar_width,
            map_size,
            scene.score,
            scene.level,
            scene.elapsed_time
        )