class BaseGame:
    def __init__(self):
        self.is_running = True
        self.is_paused = False
        self.objects = []

    def handle_event(self, event):
        pass

    def update(self):
        if not self.is_paused:
            for obj in self.objects:
                obj.update()

    def draw(self, screen):
        for obj in self.objects:
            obj.draw(screen)

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

    def restart(self):
        self.objects.clear()

    def exit(self):
        self.is_running = False