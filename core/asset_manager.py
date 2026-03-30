# Project_PBO_Game\core\asset_manager.py
import pygame
import os
import random

class AssetManager:
    def __init__(self):
        BASE_DIR = os.path.dirname(__file__)
        self.main_path = os.path.join(BASE_DIR, "../assets/main")

        self.images = {}

        self.music_list = [
            "Spiral by Loongman【8-Bit】.ogg",
            "Nobody by OneRepublic【8-Bit】.ogg",
            "Queen Bee by Mephisto【8 Bit】.ogg",
            "The Brave by Yoasobi 【8 Bit】.ogg",
            "Be a Flower by Ryokuoushoku Shakai【8-Bit】.ogg",
        ]

        self.current_music = None
        self.is_playing = False
        self.delay_time = 0 #delay music
        self.waiting = False

    # ================= IMAGE =================
    def load_image(self, filename):
        path = os.path.join(self.main_path, filename)

        if path not in self.images:
            self.images[path] = pygame.image.load(path).convert()

        return self.images[path]

    # ================= MUSIC =================
    def play_random_music(self, volume=0.3):
        if self.is_playing:
            return

        next_music = random.randint(0, len(self.music_list) - 1)
        while next_music == self.current_music:
            next_music = random.randint(0, len(self.music_list) - 1)

        self.current_music = next_music
        self._play(self.current_music, volume)

    def _play(self, index, volume):
        music_path = os.path.join(self.main_path, self.music_list[index])

        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play()  

        self.is_playing = True

    def update_music(self):
        if not pygame.mixer.music.get_busy() and self.is_playing and not self.waiting:
            self.waiting = True
            self.wait_start = pygame.time.get_ticks()

        if self.waiting:
            now = pygame.time.get_ticks()

            if now - self.wait_start >= self.delay_time:
                self.waiting = False
                self.delay_time = random.randint(2000, 4000)

                next_music = random.randint(0, len(self.music_list) - 1)
                while next_music == self.current_music:
                    next_music = random.randint(0, len(self.music_list) - 1)

                self.current_music = random.randint(0, len(self.music_list) - 1)
                self._play(self.current_music, pygame.mixer.music.get_volume())

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.wait_start = 0

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)