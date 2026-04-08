# Project_PBO_Game\games\snake\snake_game.py
import pygame
from core.base_game import BaseGame
from games.snake.snake_scene import SnakeScene
from games.snake.snake_assets import SnakeAssets

class SnakeGame(BaseGame):
    def __init__(self, game_manager):
        super().__init__()

        self.game_manager = game_manager
        self.graph = True

        self.assets = SnakeAssets(self.game_manager.asset)
        self.scene = SnakeScene(self.game_width, self.game_height, self, self.assets)

    def get_title(self):
        return "SNAKE GAME"

    def get_info_text(self):
        return [
            "",
            "--- CARA BERMAIN ---",
            "• Gunakan Tombol ARROW atau WASD",
            "• Makan kelinci untuk menambah skor",
            "• Hindari tubuh sendiri",
            "",
            "--- KONTROL ---",
            "• ARROW / WASD : Gerak",
            "• ESC          : Pause",
            "• R            : Restart",
            "• M            : Mute",
            "",
            "--- ATURAN GAME ---",
            "• Makan kelinci menambah panjang tubuh",
            "• Game Over jika menabrak tubuh sendiri",
            "• Bisa menembus tembok",
            "",
            "--- INFORMASI LEVEL ---",
            "• EASY   : Gerakan lambat",
            "• MEDIUM : Kecepatan meningkat",
            "• HARD   : Sangat cepat",
            "",
            "Design by: Fauzan Adhim Muntazhar (003) TIA25"
        ]