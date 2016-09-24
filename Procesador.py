class Procesador:
    def procesar(self, lista):

        if lista == "":
            '''Cuando viene vacía la lista se retorna el arreglo con [0,0]'''
            return [0, 0, 0, 0]
        else:
            '''Recibo la lista y hago un split para eliminar las ',' entonces,
            utilizo len para saber el número de datos'''
            datos = str.split(lista, ',')
            '''Ahora se necesita retornar el mínimo, más el arreglo.
            Utilizamos la variable auxiliar para guardar el nuevo arreglo datos'''
            auxiliar = [int(i) for i in datos]
            '''Utilizamos la nueva funcion min para hallar el mínimo, usamos max para el máximo'''
            return [len(auxiliar), min(auxiliar), max(auxiliar) , (sum(auxiliar)/float(len(auxiliar)))]
