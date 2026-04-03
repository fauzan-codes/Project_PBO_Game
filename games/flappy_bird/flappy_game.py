# .\games\flappy_bird\flappy_game.py
import pygame
from core.base_game import BaseGame
from games.flappy_bird.flappy_scene import FlappyScene

class FlappyGame(BaseGame):
    def __init__(self, game_manager):
        super().__init__()

        self.game_manager = game_manager
        self.scene = FlappyScene(self.game_width, self.game_height, self)

    def get_title(self):
        return "FLAPPY BIRD"

    def get_info_text(self):
        return [
            "",
            "--- CARA BERMAIN ---",
            "• Tekan SPACE untuk lompat",
            "• Hindari pipa",
            "",
            "--- ATURAN ---",
            "• Jangan jatuh",
            "• Jangan kena pipa",
            "",
            "Coming soon..."
        ]