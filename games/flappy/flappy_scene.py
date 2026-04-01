import pygame

class FlappyScene:
    def __init__(self, width, height, game):
        self.width = width
        self.height = height
        self.game = game

        self.font = pygame.font.Font(None, 60)

    def handle_event(self, event, mouse_pos):
        pass

    def update(self):
        pass

    def draw(self, surface):
        # background hijau
        surface.fill((0, 150, 0))

        # tulisan
        text = self.font.render("FLAPPY BIRD", True, (255, 255, 255))
        surface.blit(
            text,
            (self.width // 2 - text.get_width() // 2,
             self.height // 2 - text.get_height() // 2)
        )