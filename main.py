# Project_PBO_Game\main.py
import sys
import os

sys.path.append(os.path.dirname(__file__))

import pygame
from game_manager import GameManager
from scenes.home import Home

pygame.mixer.init()
pygame.init()

WIDTH = 1024
HEIGHT = 768

MIN_WIDTH = 1000
MIN_HEIGHT = 680

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Game Collection PBO")

game_canvas = pygame.Surface((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# INIT SYSTEM
game_manager = GameManager()
game_manager.current_scene = Home(game_manager)




running = True
while running:
    screen.fill((0, 0, 0))


    if game_manager.current_game and not game_manager.current_game.is_running:
        game_manager.unload_game()


    if game_manager.current_game:
        current = game_manager.current_game
    else:
        current = game_manager.current_scene

    if current is None:
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            new_width = max(MIN_WIDTH, event.w)
            new_height = max(MIN_HEIGHT, event.h)

            screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

            # print(f"[RESIZE]: {new_width}x{new_height}")

            if game_manager.current_game:
                game_manager.current_game.update_screen_size()

        if not game_manager.is_transitioning:
            current.handle_event(event)

    current.update()
    current.draw(screen)

    # TRANSITION
    game_manager.update_transition() 
    game_manager.draw_transition(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()