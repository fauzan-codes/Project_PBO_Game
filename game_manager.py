class GameManager:
    def __init__(self):
        self.current_game = None
        self.current_scene = None

    def load_game(self, game):
        self.current_game = game

    def unload_game(self):
        self.current_game = None

    def handle_event(self, event):
        if self.current_game:
            self.current_game.handle_event(event)

    def update(self):
        if self.current_game:
            self.current_game.update()

    def draw(self, screen):
        if self.current_game:
            self.current_game.draw(screen)