import sys
import os

sys.path.append(os.path.dirname(__file__))


import pygame
from game_manager import GameManager
from scenes.menu import Menu

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Collection PBO")

clock = pygame.time.Clock()

# INIT SYSTEM
game_manager = GameManager()
menu = Menu(game_manager)

current_scene = menu  # awalnya menu
if game_manager.current_game:
    current_scene = game_manager.current_game
else:
    current_scene = menu

running = True
while running:
    screen.fill((0, 0, 0))

    if game_manager.current_game and not game_manager.current_game.is_running:
        game_manager.unload_game()

    # SWITCH SCENE
    if game_manager.current_game:
        current_scene = game_manager.current_game
    else:
        current_scene = menu

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        current_scene.handle_event(event)

    current_scene.update()
    current_scene.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()