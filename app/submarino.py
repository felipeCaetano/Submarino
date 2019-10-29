class Submarino():
    hangs = ["NORTH", "EAST", "SOUTH", "WEST"]

    def __init__(self):
        self.pos_X = 0
        self.pos_Y = 0
        self.pos_Z = 0
        self.direction = self.hangs[0]

    def informar_posicao(self):
        return [self.pos_X, self.pos_Y, self.pos_Z, self.direction]

    def turn(self, hang):
        if hang == 'L':
            h = self.hangs.index(self.direction) - 1
            self.direction = self.hangs[h % 4]
        else:
            h = self.hangs.index(self.direction) + 1
            self.direction = self.hangs[h % 4]

    def move(self):
        if self.direction == 'NORTH':
            self.pos_Y += 1
        elif self.direction == 'SOUTH':
            self.pos_Y -= 1
        elif self.direction == "EAST":
            self.pos_X += 1
        elif self.direction == "WEST":
            self.pos_X -= 1

    def down(self, hang):
        if hang == 'D':
            self.pos_Z -= 1
        if hang == 'U' and self.pos_Z < 0:
            self.pos_Z += 1
