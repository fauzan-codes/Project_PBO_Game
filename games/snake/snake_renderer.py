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