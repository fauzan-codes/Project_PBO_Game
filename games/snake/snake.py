# Project_PBO_Game\games\snake\snake.py
from core.game_object import GameObject

class Snake(GameObject):
    def __init__(self, grid_width, grid_height, level="easy"):
        super().__init__(0, 0)

        self.grid_width = grid_width
        self.grid_height = grid_height

        start_x = grid_width // 2
        start_y = grid_height // 2

        self.body = [
            (start_x, start_y),
            (start_x - 1, start_y),
            (start_x - 2, start_y),
        ]

        self.direction = (1, 0)
        self.next_direction = (1, 0)

        # level status
        self.level = level
        self.move_delay = 12
        self.min_delay = 5   #max speed
        self.speed_step = 1  #speed

        self.move_timer = 0
        self.grow = False

        self.setup_level()

    
    def set_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.next_direction = direction

    
    def update(self):
        self.move_timer += 1

        if self.move_timer >= self.move_delay:
            self.move_timer = 0
            self.move()

    
    def move(self):
        self.direction = self.next_direction

        head_x, head_y = self.body[0]
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)

        # tembok
        new_head = (
            new_head[0] % self.grid_width,
            new_head[1] % self.grid_height
        )

        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    
    def eat(self):
        self.grow = True

    
    def check_self_collision(self):
        head = self.body[0]
        return head in self.body[1:]
    

    def setup_level(self):
        if self.level == "Easy":
            self.move_delay = 12
            self.min_delay = 12   

        elif self.level == "Medium":
            self.move_delay = 12
            self.min_delay = 6    

        elif self.level == "Hard":
            self.move_delay = 8
            self.min_delay = 4    


    def increase_speed(self):
        if self.level == "easy":
            return

        if self.move_delay > self.min_delay:
            self.move_delay -= self.speed_step

            if self.move_delay < self.min_delay:
                self.move_delay = self.min_delay
    

    def draw(self, surface):
        pass