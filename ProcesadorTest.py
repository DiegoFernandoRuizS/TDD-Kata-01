from unittest import TestCase

from Procesador import *
class ProcesadorTest(TestCase):
    def test_procesador(self):
        self.assertEquals(Procesador().procesar(""), 0, "Lista sin datos")
