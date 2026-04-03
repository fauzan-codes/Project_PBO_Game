# .\games\flappy_bird\flappy_animation.py

class FlappyAnimation:
    def __init__(self):
        self.offset = 0

    def update(self):
        self.offset += 0.5

    def get_idle_offset(self):
        import math
        return math.sin(self.offset) * 10