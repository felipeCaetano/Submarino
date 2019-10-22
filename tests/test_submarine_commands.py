from unittest import TestCase
from app.submarino import Submarino


class SubmarineCommandTester(TestCase):
    def setUp(self):
        self.submarino = Submarino()

    def test_informar_sua_posicao_deve_retornar_uma_lista(self):
        self.assertListEqual(
            self.submarino.informar_posicao(), [0, 0, 0, "NORTH"])

    # def test_girar_deve_aceitar_parametro(self):

    def test_girar_deve_mudar_a_direcao_do_submarino(self):
        self.submarino.turn('L')
        self.assertEqual(self.submarino.informar_posicao(), [0, 0, 0, "WEST"])
        self.submarino.turn('R')
        self.assertEqual(self.submarino.informar_posicao(), [0, 0, 0, "NORTH"])

    def test_move_deve_mover_o_submarino_para_onde_esta_apontando(self):
        self.submarino.move()
        self.assertEqual(self.submarino.informar_posicao(), [0, 1, 0, "NORTH"])

    def test_down_deve_submergir_e_emegir_o_submarino(self):
        self.submarino.down('D')
        self.assertEqual(
            self.submarino.informar_posicao(), [0, 0, -1, "NORTH"])
        self.submarino.down('U')
        self.assertEqual(self.submarino.informar_posicao(), [0, 0, 0, "NORTH"])

    def test_submarinos_nao_voam(self):
        self.submarino.down('U')
        self.submarino.down('U')
        self.assertEqual(self.submarino.informar_posicao(), [0, 0, 0, "NORTH"])
