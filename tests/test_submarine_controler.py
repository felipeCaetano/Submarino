from unittest import TestCase
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
    
