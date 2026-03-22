import pygame

class SnakeAssets:
    def __init__(self):
        self.size = 16

        # load sprite
        self.sprite1 = pygame.image.load("assets/Snake/snake.png").convert_alpha()
        self.sprite2 = pygame.image.load("assets/Snake/snake2.png").convert_alpha()

        # slice
        self.tiles1 = self.slice(self.sprite1)
        self.tiles2 = self.slice(self.sprite2)

        # animasi
        self.frame_index = 0
        self.timer = 0

    def slice(self, image):
        tiles = []
        for y in range(0, image.get_height(), self.size):
            for x in range(0, image.get_width(), self.size):
                rect = pygame.Rect(x, y, self.size, self.size)
                tiles.append(image.subsurface(rect))
        return tiles

    def update(self):
        self.timer += 1
        if self.timer > 50:
            self.timer = 0
            self.frame_index = (self.frame_index + 1) % 2

    def get_tiles(self):
        return self.tiles1 if self.frame_index == 0 else self.tiles2

    # ================== GET SPRITES ==================

    def get_head(self, direction): # kepala
        tiles = self.get_tiles()
        return tiles[direction]

    def get_tail(self, direction): #ekor
        tiles = self.get_tiles()
        return tiles[4 + direction]

    def get_body_straight(self, direction): #badan 
        tiles = self.get_tiles()
        if direction in [(0,1), (0,-1)]:  # vertical
            return tiles[12]
        else:
            return tiles[13]

    def get_turn(self, prev_dir, next_dir):
        tiles = self.get_tiles()

        mapping = {
            ((0, -1), (1, 0)): 9,   # atas → kanan
            ((1, 0), (0, -1)): 11,

            ((0, 1), (1, 0)): 8,    # bawah → kanan
            ((1, 0), (0, 1)): 10,

            ((-1, 0), (0, 1)): 9,  # kiri → bawah
            ((0, 1), (-1, 0)): 11,

            ((-1, 0), (0, -1)): 8, # kiri → atas
            ((0, -1), (-1, 0)): 10,
        }

        key = (prev_dir, next_dir)
        if key in mapping:
            return tiles[mapping[key]]
        else:
            # fallback biar gak crash
            return tiles[12]  # body vertical default
        

    def get_food(self): #makann/kelinci
        return self.get_tiles()[14]

    def get_bg(self): #background
        return self.get_tiles()[15]