from unittest import TestCase
from unittest.mock import patch

from app import controller, submarino


class SubmarineControllerTester(TestCase):
    def setUp(self):
        sub = submarino.Submarino()
        self.controller = controller.Controller(sub)

    def test_controlador_deve_exitir(self):
        self.assertEqual(
            hasattr(controller, 'Controller'),
            True,
            'Controller deve existir...'
            )

    def test_controller_deve_ser_callable(self):
        self.assertEqual(
            hasattr(controller.Controller, '__call__'),
            True,
            'Controller deve ser callable...'
            )

    def test_controller_dever_ter_um_submarino(self):

        self.assertEqual(
            hasattr(self.controller, 'submarino'),
            True,
            'Controller deve ter um submarino...'
            )

    def test_controller_deve_receber_comandos(self):
        self.assertEqual(
            hasattr(self.controller, 'receber_comandos'),
            True,
            'Controller deve receber comandos...'
            )

    def test_controller_receber_comandos_deve_ler_uma_string(self):
        command_input = 'DDMMRMLLM'
        with patch('builtins.input', return_value=command_input):
            stacks = self.controller.receber_comandos()
        self.assertEqual(stacks, command_input)

    def test_controller_deve_ter_uma_funcao_girar(self):
        self.assertEqual(
            hasattr(self.controller, 'turn_submarine'),
            True,
            'Controller deve girar o submarino'
        )

    def test_controller_deve_ter_uma_funcao_submergir(self):
        self.assertEqual(
            hasattr(self.controller, 'down_submarine'),
            True,
            'Controller deve submergir o submarino'
        )

    def test_controller_deve_obter_a_posicao_do_submarino(self):
        self.assertEqual(
            hasattr(self.controller, 'pos_submarine'),
            True,
            'Controller deve solicitar a posição do submarino'
        )
        self.assertEqual(
            self.controller.pos_submarine(),
            self.controller.submarino.informar_posicao(),
            'O controlador deve obter a posição do submarino'
        )

    def test_controller_deve_ter_uma_funcao_avancar(self):
        self.assertEqual(
            hasattr(self.controller, 'move_submarine'),
            True,
            'Controller deve avançar o submarino'
        )

    def test_controller_down_deve_mudar_posz(self):
        command_input = 'D'
        with patch('builtins.input', return_value=command_input):
            self.controller.down_submarine(command_input)
        self.assertEqual(self.controller.pos_submarine(), [0, 0, -1, 'NORTH'])

    def test_controller_move_deve_mudar_posy_se_direction_north(self):
        command_input = 'M'
        with patch('builtins.input', return_value=command_input):
            self.controller.move_submarine()
        self.assertEqual(self.controller.pos_submarine(), [0, 1, 0, 'NORTH'])

    def test_controller_move_deve_mudar_posy_direction_se_command_L(self):
        command_input = 'L'
        with patch('builtins.input', return_value=command_input):
            self.controller.turn_submarine(command_input)
        self.assertEqual(self.controller.pos_submarine(), [0, 0, 0, 'WEST'])

    def test_receber_comandos_deve_chamar_as_funcoes_correspondentes(self):
        command_input = 'DMRL'
        with patch('builtins.input', return_value=command_input):
            self.controller.tratador()
        self.assertEqual(self.controller.pos_submarine(), [0, 1, -1, 'NORTH'])

    def test_controller_entrada1(self):
        command_input = 'LMRDDMMUU'
        with patch('builtins.input', return_value=command_input):
            self.controller.tratador()
        self.assertEqual(self.controller.pos_submarine(), [-1, 2, 0, 'NORTH'])

    def test_controller_entrada2(self):
        command_input = 'RMMLMMMDDLL'
        with patch('builtins.input', return_value=command_input):
            self.controller.tratador()
        self.assertEqual(self.controller.pos_submarine(), [2, 3, -2, 'SOUTH'])
