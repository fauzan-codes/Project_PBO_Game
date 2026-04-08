# .\games\flappy_bird\flappy_game.py
import pygame
from core.base_game import BaseGame
from games.flappy_bird.flappy_scene import FlappyScene
from games.flappy_bird.flappy_assets import FlappyAssets

class FlappyGame(BaseGame):
    def __init__(self, game_manager):
        super().__init__()

        self.game_manager = game_manager
        self.assets = FlappyAssets(self.game_manager.asset)
        self.graph = False
        self.scene = FlappyScene(self.game_width, self.game_height, self, self.assets)

    def get_title(self):
        return "FLAPPY BIRD"

    def get_info_text(self):
        return [
            "",
            "--- CARA BERMAIN ---",
            "• Klik game area untuk masuk ke game",
            "• Tekan SPACE untuk mulai",
            "• Tekan SPACE atau Klik Mouse untuk lompat",
            "• Lewati pipa untuk mendapatkan skor",
            "",
            "--- KONTROL ---",
            "• SPACE   : Lompat",
            "• Mouse(L): Lompat",
            "• ESC     : Pause",
            "• R       : Restart",
            "• M            : Mute",
            "",
            "--- ATURAN GAME ---",
            "• Jangan menabrak pipa",
            "• Jangan jatuh ke tanah",
            "• Skor bertambah setiap melewati pipa",
            "",
            "--- INFORMASI LEVEL ---",
            "• Kecepatan pipa meningkat seiring skor",
            "• Game semakin sulit semakin lama bermain",
            "",
            "Design by: Fauzan Adhim Muntazhar (003) TIA25"
        ]