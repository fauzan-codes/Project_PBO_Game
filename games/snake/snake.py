import random

class Snake:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height

        # mulai dari tengah
        start_x = grid_width // 2
        start_y = grid_height // 2

        self.body = [
            (start_x, start_y),
            (start_x - 1, start_y),
            (start_x - 2, start_y),
        ]

        self.direction = (1, 0)
        self.next_direction = (1, 0)

        # movement speed
        self.move_delay = 10
        self.move_timer = 0

        self.grow = False

    # ================= INPUT =================
    def set_direction(self, direction):
        # cegah balik arah langsung
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.next_direction = direction

    # ================= UPDATE =================
    def update(self):
        self.move_timer += 1

        if self.move_timer >= self.move_delay:
            self.move_timer = 0
            self.move()

    # ================= MOVE =================
    def move(self):
        self.direction = self.next_direction

        head_x, head_y = self.body[0]
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)

        # wrap map (tembus tembok)
        new_head = (
            new_head[0] % self.grid_width,
            new_head[1] % self.grid_height
        )

        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    # ================= GROW =================
    def eat(self):
        self.grow = True

    # ================= COLLISION =================
    def check_self_collision(self):
        head = self.body[0]
        return head in self.body[1:]