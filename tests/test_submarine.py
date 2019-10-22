from unittest import TestCase
from app import submarino


class SubmarineTester(TestCase):
    def setUp(self):
        self.submarino = submarino.Submarino()

    def test_submarino_deve_existir(self):
        self.assertEqual(
            hasattr(submarino, 'Submarino'),
            True,
            'Submarino deve existir'
            )

    def test_submarino_deve_ser_callable(self):
        self.assertEqual(
            hasattr(submarino.Submarino, "__call__"),
            True,
            "Submarino deve ser invocável"
        )

    def test_submarino_deve_ter_atributo_posx(self):
        self.assertEqual(
            hasattr(self.submarino, 'pos_X'),
            True,
            "Atributo pos_X não foi criado!"
        )

    def test_submarino_deve_ter_atributo_posy(self):
        self.assertEqual(
            hasattr(self.submarino, 'pos_Y'),
            True,
            "Atributo pos_Y não foi criado!"
        )

    def test_submarino_deve_ter_atributo_posz(self):
        self.assertEqual(
            hasattr(self.submarino, 'pos_Z'),
            True,
            "Atributo pos_Z não foi criado!"
        )

    def test_submarino_deve_ter_atributo_direction(self):
        self.assertEqual(
            hasattr(self.submarino, 'direction'),
            True,
            "Atributo direction não foi criado!"
        )

    def test_submarino_deve_informar_sua_posicao(self):
        self.assertEqual(
            hasattr(self.submarino, 'informar_posicao'),
            True,
            "Não existe metodo informar_posicao"
        )

    def test_submarino_deve_ser_capaz_de_girar(self):
        self.assertEqual(
            hasattr(self.submarino, 'turn'),
            True,
            "Não existe metodo turn..."
        )

    def test_submarino_deve_ser_capaz_de_avancar(self):
        self.assertEqual(
            hasattr(self.submarino, 'move'),
            True,
            "Não existe metodo move..."
        )

    def test_submarino_deve_ser_capaz_de_submergir(self):
        self.assertEqual(
            hasattr(self.submarino, 'down'),
            True, "Não existe metodo de submergir..."
        )
