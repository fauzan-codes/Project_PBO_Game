# .\games\dino_run\dino_game.py
import pygame
from core.base_game import BaseGame
from games.dino_run.dino_scene import DinoScene
from games.dino_run.dino_assets import DinoAssets

class DinoGame(BaseGame):
    def __init__(self, game_manager):
        super().__init__()

        self.game_manager = game_manager
        self.graph = True

        self.assets = DinoAssets(self.game_manager.asset)
        self.scene = DinoScene(self.game_width, self.game_height, self, self.assets)

    def get_title(self):
        return "DINO RUN"

    def get_info_text(self):
        return [
            "",
            "--- CARA BERMAIN ---",
            "• Tekan SPACE untuk mulai",
            "• Tekan SPACE atau UP untuk melompat",
            "• Tekan DOWN untuk menunduk",
            "• Hindari kaktus dan burung",
            "",
            "--- KONTROL ---",
            "• SPACE / UP : Lompat",
            "• DOWN       : Menunduk",
            "• ESC        : Pause",
            "• R          : Restart",
            "• M          : Mute",
            "",
            "--- ATURAN GAME ---",
            "• Jangan menabrak kaktus",
            "• Jangan menabrak burung",
            "• Skor bertambah seiring waktu",
            "• Kecepatan meningkat seiring skor",
            "",
            "--- INFORMASI LEVEL ---",
            "• Bird muncul setelah score 400",
            "• Speed meningkat secara bertahap",
            "• Game semakin cepat seiring waktu",
            "",
            "Design by: Fauzan Adhim Muntazhar (003) TIA25"
        ]