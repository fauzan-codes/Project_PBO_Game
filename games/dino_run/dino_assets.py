# .\games\dino_run\dino_assets.py
import pygame
import os


class DinoAssets:
    def __init__(self, asset_manager):
        self.asset_manager = asset_manager
        BASE_DIR = os.path.dirname(__file__)

        self.dino_run = [
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/dinoRun/Dino1.png")),
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/dinoRun/Dino2.png")),
        ]

        self.dino_duck = [
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/dinoRun/DinoDucking1.png")),
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/dinoRun/DinoDucking2.png")),
        ]

        self.dino_jump = pygame.image.load(os.path.join(BASE_DIR, "../../assets/dinoRun/DinoJumping.png"))

        self.cactus = [
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/dinoRun/cactus1.png")),
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/dinoRun/cactus2.png")),
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/dinoRun/cactus3.png")),
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/dinoRun/cactus4.png")),
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/dinoRun/cactus5.png")),
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/dinoRun/cactus6.png")),
        ]

        self.bird = [
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/dinoRun/bird.png")),
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/dinoRun/bird2.png")),
        ]

        self.cloud = pygame.image.load( os.path.join(BASE_DIR, "../../assets/dinoRun/cloud.png"))
        self.ground = pygame.image.load(os.path.join(BASE_DIR, "../../assets/dinoRun/ground.png"))

        self.font_path = os.path.join(BASE_DIR,"../../assets/dinoRun/PressStart2P-Regular.ttf")
        self.font_small = pygame.font.Font(self.font_path, 20)
        self.font_medium = pygame.font.Font(self.font_path, 30)
        self.font_big = pygame.font.Font(self.font_path, 50)

        # sfx
        self.sfx_jump = pygame.mixer.Sound(os.path.join(BASE_DIR, "../../assets/dinoRun/jump.mp3"))
        self.sfx_score = pygame.mixer.Sound(os.path.join(BASE_DIR, "../../assets/dinoRun/100points.mp3"))
        self.sfx_lose = pygame.mixer.Sound(os.path.join(BASE_DIR, "../../assets/dinoRun/lose.mp3"))

        # register sound
        self.asset_manager.register_sound(self.sfx_jump)
        self.asset_manager.register_sound(self.sfx_score)
        self.asset_manager.register_sound(self.sfx_lose)

        # volume
        self.sfx_jump.set_volume(0.5)
        self.sfx_score.set_volume(0.5)
        self.sfx_lose.set_volume(0.5)

        self.frame_index = 0
        self.timer = 0


    def update(self):
        self.timer += 1
        if self.timer > 10:
            self.timer = 0
            self.frame_index = (self.frame_index + 1) % 2

    # dino
    def get_run(self):
        return self.dino_run[self.frame_index]

    def get_duck(self):
        return self.dino_duck[self.frame_index]

    def get_jump(self):
        return self.dino_jump

    # bird 
    def get_bird(self):
        return self.bird[self.frame_index]

    # kaktus
    def get_random_cactus(self):
        import random
        return random.choice(self.cactus)

    # font
    def get_font(self, size):
        return pygame.font.Font(self.font_path, size)

    # sfx
    def play_jump(self):
        self.sfx_jump.play()

    def play_score(self):
        self.sfx_score.play()

    def play_lose(self):
        self.sfx_lose.play()
