# Project_PBO_Game\games\snake\snake_game.py
import pygame
from core.base_game import BaseGame
from games.snake.snake_scene import SnakeScene
from games.snake.snake_assets import SnakeAssets

class SnakeGame(BaseGame):
    def __init__(self, game_manager):
        super().__init__()

        self.game_manager = game_manager

        self.scene = SnakeScene(self.game_width, self.game_height, self)
        self.assets = SnakeAssets()

    def get_title(self):
        return "SNAKE GAME"

    def get_info_text(self):
        return [
            "",
            "--- CARA BERMAIN ---",
            "• Gerakan: Gunakan Tombol ARROW atau WASD pada Keyboard",
            "• Pause    : Tekan ESC saat bermain",
            "• Restart   : Tekan R saat mode Pause atau Game Over",
            "",
            "--- ATURAN GAME ---",
            "• Makan kelinci untuk menambah skor dan panjang tubuh.",
            "• Game Over jika kepala menabrak tubuh sendiri.",
            "• Bisa menembus tembok",
            "",
            "--- INFORMASI LEVEL ---",
            "• EASY     : Gerakan lambat dan tetap.",
            "• MEDIUM : Kecepatan standar, bertambah jika score tinggi.",
            "• HARD     : Gerakan sangat cepat, akan semakin cepat lagi",
            "",
            "",
            "Design by: Fauzan Adhim Muntazhar (003) TIA25"
        ]