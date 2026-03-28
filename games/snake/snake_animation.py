# Project_PBO_Game\games\snake\snake_animation.py
class SnakeAnimation:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.body = [(0,5), (-1,5), (-2,5)]
        self.dir = (1,0)

        self.timer = 0
        self.delay = 8

        self.patterns = [
            [(1,0)]*14 + [(0,1)]*20 + [(-1,0)]*12 + [(0,1)]*15,
            [(1,0)]*10 + [(0,1)]*14 + [(1,0)]*18 + [(0,-1)]*12,
            [(1,0)]*10 + [(0,1)]*10 + [(-1,0)]*8 + [(0,-1)]*6 + [(1,0)]*4,
        ]

        self.pattern_index = 0
        self.step = 0
        self.length = 6

    def update(self):
        self.timer += 1
        if self.timer < self.delay:
            return

        self.timer = 0

        pattern = self.patterns[self.pattern_index]
        next_dir = pattern[self.step]

        if (next_dir[0]*-1, next_dir[1]*-1) == self.dir:
            next_dir = self.dir

        self.dir = next_dir
        self.step += 1

        if self.step >= len(pattern):
            self.step = 0
            self.pattern_index = (self.pattern_index + 1) % len(self.patterns)

        head_x, head_y = self.body[0]
        dx, dy = self.dir

        new_head = (
            (head_x + dx) % (self.width // 16),
            (head_y + dy) % (self.height // 16)
        )

        self.body.insert(0, new_head)

        if len(self.body) > self.length:
            self.body.pop()