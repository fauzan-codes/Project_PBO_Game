# .\games\dino_run\dino_game.py
import pygame
from core.base_game import BaseGame
from games.dino_run.dino_scene import DinoScene
from games.dino_run.dino_assets import DinoAssets

class DinoGame(BaseGame):
    def __init__(self, game_manager):
        super().__init__()

        self.game_manager = game_manager

        self.assets = DinoAssets()
        self.scene = DinoScene(self.game_width, self.game_height, self, self.assets)

    def get_title(self):
        return "DINO RUN"

    def get_info_text(self):
        return [
            "",
            "--- CARA BERMAIN ---",
            "",
            "--- ATURAN GAME ---",
            "",
            "--- INFORMASI LEVEL ---",
            "",
            "",
            "Design by: Fauzan Adhim Muntazhar (003) TIA25"
        ]