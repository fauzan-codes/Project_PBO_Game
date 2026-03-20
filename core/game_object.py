class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.active = True

    def update(self):
        pass

    def draw(self, screen):
        pass

    def destroy(self):
        self.active = False