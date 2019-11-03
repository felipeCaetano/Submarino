from app.submarino import Submarino


class Controller():
    def __init__(self, sub: Submarino):
        self.submarino = sub

    def receber_comandos(self):
        command = input()
        return command

    def tratador(self):
        seq = self.receber_comandos()
        unit = (x for x in seq)
        for uc in unit:
            if uc == "D" or uc == 'U':
                self.down_submarine(uc)
            elif uc == 'R' or uc == 'L':
                self.turn_submarine(uc)
            elif uc == 'M':
                self.move_submarine()

    def turn_submarine(self, command):
        self.submarino.turn(command)

    def down_submarine(self, command):
        self.submarino.down(command)

    def move_submarine(self):
        self.submarino.move()

    def pos_submarine(self):
        return self.submarino.informar_posicao()
