# .\games\flappy_bird\flappy_renderer.py

class FlappyRenderer:
    def __init__(self, width, height, assets):
        self.width = width
        self.height = height
        self.assets = assets

    def draw_background(self, screen, bg_x):
        bg_width = self.assets.background.get_width()
        for i in range(-1, self.width // bg_width + 2):
            screen.blit(self.assets.background, (bg_x + i * bg_width, 0))

    def draw_ground(self, screen, ground_x, ground_y):
        ground_width = self.assets.ground.get_width()
        for i in range(-1, self.width // ground_width + 2):
            screen.blit(self.assets.ground, (ground_x + i * ground_width, ground_y))

    def draw_pipes(self, screen, pipes):
        for pipe in pipes:
            pipe.draw(screen)

    def draw_bird(self, screen, bird):
        bird.draw(screen)