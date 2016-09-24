from unittest import TestCase

from Procesador import *


class ProcesadorTest(TestCase):
    def test_procesador(self):
        self.assertEquals(Procesador().procesar(""), [0,0], "Lista sin datos")

    def test_procesador_1(self):
        self.assertEquals(Procesador().procesar("2"), [1,2], "Lista con 1 dato")

    def test_procesador_2(self):
        self.assertEquals(Procesador().procesar("3,0"), [2,0], "Lista con 2 datos")

    def test_procesador_n(self):
        self.assertEquals(Procesador().procesar("1,2,3,4"), [4,1], "Lista con 4 datos")
