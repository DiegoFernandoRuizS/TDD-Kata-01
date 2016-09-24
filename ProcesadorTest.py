from unittest import TestCase

from Procesador import *


class ProcesadorTest(TestCase):
    def test_procesador(self):
        self.assertEquals(Procesador().procesar(""), 0, "Lista sin datos")

    def test_procesador_1(self):
        self.assertEquals(Procesador().procesar("1"), 1, "Lista con 1 dato")
