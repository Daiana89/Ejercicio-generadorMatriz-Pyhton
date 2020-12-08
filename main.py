#Ejercicio dos
#Generar una clase denominada Matriz la cual reciba 3 parámetros un
#parámetro para la cantidad de filas, un parámetro para cantidad de
#columnas y un tercer parámetro opcional que nos indica el valor con el
#cual se inicializara la matriz si no se indica se debe inicializar toda la
#matriz con ceros.

class matriz():
    def __init__ (self, filas, columnas, iniciar=0):
        self.filas = filas
        self.columnas = columnas
        self.iniciar = iniciar
        self.matris = []

    def crear (self):
        if self.iniciar == 0:
            for x in range(self.filas):
                self.matris.append([0] * self.columnas)
        else:
            for x in range(self.filas):
                self.matris.append([self.iniciar] * self.columnas)
        print(self.matris)
        
    
matriz = matriz(4,5,6)  

matriz.crear()