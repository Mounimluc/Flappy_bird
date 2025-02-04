import py5

class pipe:
    def __init__(self):
        self.width = 40
        self.gap = py5.random_int(50, 100)
        self.pos_x = py5.width + self.width
        self.pos_y = 0
        self.is_passed = False

    def move_obstacle(self, speed):
        self.pos_x = self.pos_x + speed

    def show(self):
        py5.fill(101,155,94)
        py5.rect(self.pos_x, self.pos_y + self.gap, self.width, py5.height)
        py5.rect(self.pos_x, self.pos_y - self.gap, self.width, -py5.height)

    def collision_check(self, body):
        if body.pos_x > self.pos_x and body.pos_x < self.pos_x + self.width:
            if (body.pos_y > self.pos_y + self.gap):
                return True
            elif (body.pos_y < self.pos_y - self.gap):
                return True

    def check_if_passed(self, body):
        if body.pos_x > self.pos_x and body.pos_x < self.pos_x + self.width:
            if self.is_passed == False and not ((body.pos_y > self.pos_y + self.gap) or (body.pos_y < self.pos_y - self.gap)):
                self.is_passed = True
                return True
