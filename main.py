import sys
import os

sys.path.append(os.path.dirname(__file__))

import pygame
from game_manager import GameManager
from scenes.home import Home


pygame.init()

WIDTH = 1024
HEIGHT = 768

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Collection PBO")

clock = pygame.time.Clock()

# INIT SYSTEM
game_manager = GameManager()
game_manager.current_scene = Home(game_manager)




running = True
while running:
    screen.fill((0, 0, 0))

    # HANDLE EXIT GAME
    if game_manager.current_game and not game_manager.current_game.is_running:
        game_manager.unload_game()

    # PILIH YANG AKTIF
    if game_manager.current_game:
        current = game_manager.current_game
    else:
        current = game_manager.current_scene

    if current is None:
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        current.handle_event(event)

    current.update()
    current.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()