import pygame

class SnakeAssets:
    def __init__(self):
        # load sprite
        self.snake_img = pygame.image.load("assets/Snake/snake.png").convert_alpha()
        self.snake2_img = pygame.image.load("assets/Snake/snake2.png").convert_alpha()

        # ukuran per segment (kita asumsi dulu, nanti bisa disesuaikan)
        self.size = 32  

        # potong sprite
        self.frames = self.slice_snake(self.snake_img)
        self.frames2 = self.slice_snake(self.snake2_img)

        self.current_frame = 0
        self.timer = 0

    def slice_snake(self, image):
        frames = []
        width = image.get_width()
        height = image.get_height()

        cols = width // self.size
        rows = height // self.size

        for y in range(rows):
            for x in range(cols):
                rect = pygame.Rect(x*self.size, y*self.size, self.size, self.size)
                frame = image.subsurface(rect)
                frames.append(frame)

        return frames

    def get_frame(self):
        self.timer += 1

        if self.timer > 10:
            self.timer = 0
            self.current_frame = (self.current_frame + 1) % 2

        if self.current_frame == 0:
            return self.frames
        else:
            return self.frames2