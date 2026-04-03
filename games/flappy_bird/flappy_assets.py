# .\games\flappy_bird\flappy_assets.py
import pygame
import os

class FlappyAssets:
    def __init__(self):
        BASE_DIR = os.path.dirname(__file__)

        # ================= IMAGE =================
        self.background = pygame.image.load(
            os.path.join(BASE_DIR, "../../assets/FlappyBird/background.png")
        )

        self.ground = pygame.image.load(
            os.path.join(BASE_DIR, "../../assets/FlappyBird/ground.png")
        )

        self.pipe = pygame.image.load(
            os.path.join(BASE_DIR, "../../assets/FlappyBird/pipe.png")
        )

        # BIRD ANIMATION (3 frame)
        self.bird_frames = [
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/FlappyBird/bird-downflap.png")),
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/FlappyBird/bird-midflap.png")),
            pygame.image.load(os.path.join(BASE_DIR, "../../assets/FlappyBird/bird-upflap.png")),
        ]

        # UI
        self.gameover = pygame.image.load(
            os.path.join(BASE_DIR, "../../assets/FlappyBird/gameover.png")
        )

        self.get_ready = pygame.image.load(
            os.path.join(BASE_DIR, "../../assets/FlappyBird/getready-text.png")
        )

        self.tap = pygame.image.load(
            os.path.join(BASE_DIR, "../../assets/FlappyBird/tap.png")
        )

        self.title = pygame.image.load(
            os.path.join(BASE_DIR, "../../assets/FlappyBird/flappybird-text.png")
        )

        self.arrow = pygame.image.load(
            os.path.join(BASE_DIR, "../../assets/FlappyBird/arrow.png")
        )

        self.bird_die = pygame.image.load(
            os.path.join(BASE_DIR, "../../assets/FlappyBird/bird-die.png")
        )

        # NUMBER (score)
        self.numbers = []
        for i in range(10):
            img = pygame.image.load(
                os.path.join(BASE_DIR, f"../../assets/FlappyBird/numbers/{i}.png")
            )
            self.numbers.append(img)

        # ================= SOUND =================
        self.sfx_die = pygame.mixer.Sound(
            os.path.join(BASE_DIR, "../../assets/FlappyBird/die.ogg")
        )
        self.sfx_hit = pygame.mixer.Sound(
            os.path.join(BASE_DIR, "../../assets/FlappyBird/hit.ogg")
        )
        self.sfx_wing = pygame.mixer.Sound(
            os.path.join(BASE_DIR, "../../assets/FlappyBird/wing.ogg")
        )
        self.sfx_swoosh = pygame.mixer.Sound(
            os.path.join(BASE_DIR, "../../assets/FlappyBird/swoosh.ogg")
        )

        # volume
        self.sfx_die.set_volume(0.5)
        self.sfx_hit.set_volume(0.5)
        self.sfx_wing.set_volume(0.5)
        self.sfx_swoosh.set_volume(0.5)

        # ================= ANIMATION =================
        self.frame_index = 0
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer > 10:
            self.timer = 0
            self.frame_index = (self.frame_index + 1) % 3

    def get_bird(self):
        return self.bird_frames[self.frame_index]
