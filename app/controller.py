from app.submarino import Submarino


class Controller():
    def __init__(self, sub: Submarino):
        self.submarino = sub

    def receber_comandos(self):
        command = list(input())
