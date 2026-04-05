# .\games\dino_run\dino_assets.py
import pygame
import os

class DinoAssets:
    def __init__(self):
        base_path = "assets/dino"

        # dino
        self.dino_run = [
            pygame.image.load(os.path.join(base_path, "../../assets/dinoRun/Dino1.png")),
            pygame.image.load(os.path.join(base_path, "../../assets/dinoRun/Dino2.png")),
        ]

        self.dino_duck = [
            pygame.image.load(os.path.join(base_path, "../../assets/dinoRun/DinoDucking1.png")),
            pygame.image.load(os.path.join(base_path, "../../assets/dinoRun/DinoDucking2.png")),
        ]

        self.dino_jump = pygame.image.load(
            os.path.join(base_path, "../../assets/dinoRun/DinoJumping.png")
        )

        # kaktus
        self.cactus = [
            pygame.image.load(os.path.join(base_path, "../../assets/dinoRun/cactus1.png")),
            pygame.image.load(os.path.join(base_path, "../../assets/dinoRun/cactus2.png")),
            pygame.image.load(os.path.join(base_path, "../../assets/dinoRun/cactus3.png")),
            pygame.image.load(os.path.join(base_path, "../../assets/dinoRun/cactus4.png")),
            pygame.image.load(os.path.join(base_path, "../../assets/dinoRun/cactus5.png")),
            pygame.image.load(os.path.join(base_path, "../../assets/dinoRun/cactus6.png")),
        ]

        # bird
        self.bird = [
            pygame.image.load(os.path.join(base_path, "../../assets/dinoRun/bird.png")),
            pygame.image.load(os.path.join(base_path, "../../assets/dinoRun/bird2.png")),
        ]

        # environment
        self.cloud = pygame.image.load(
            os.path.join(base_path, "../../assets/dinoRun/cloud.png")
        )

        self.ground = pygame.image.load(
            os.path.join(base_path, "../../assets/dinoRun/ground.png")
        )

        # SFX
        self.sfx_jump = pygame.mixer.Sound(
            os.path.join(base_path, "../../assets/dinoRun/jump.mp3")
        )

        self.sfx_score = pygame.mixer.Sound(
            os.path.join(base_path, "../../assets/dinoRun/100points.mp3")
        )

        self.sfx_lose = pygame.mixer.Sound(
            os.path.join(base_path, "../../assets/dinoRun/lose.mp3")
        )