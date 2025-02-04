import py5

class player:
    def __init__(self):
        self.pos_x = 200
        self.pos_y = 100
        self.speedy = 0
        self.baseSpeed = 2
        self.diameter = 20
        self.gravity = 0.50
        self.is_playing = True
    

    def move(self):
        self.pos_y = self.pos_y + self.speedy
        self.speedy = self.speedy + self.gravity

        if self.speedy > 20:
            self.speedy = 20
    

    def jump(self):
        if py5.is_key_pressed and self.speedy > -1 :
            if py5.key in ['z', 'Z']:
                self.speedy = self.speedy - 8


    def show(self):
        py5.fill(250,199,72)
        py5.ellipse(self.pos_x, self.pos_y, self.diameter, self.diameter)
    




