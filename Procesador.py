class Procesador:
    def procesar(self, lista):

        if lista == "":
            return [0, 0]
        else:
            '''Recibo la lista y hago un split para eliminar las ',' entonces,
            utilizo len para saber el número de datos'''
            datos = str.split(lista, ',')
            return {len(datos)}
