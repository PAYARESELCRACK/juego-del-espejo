class HUB:
    def __init__(self, tablero):
        self.matriz = tablero

    def principal(self):
        print("\t\t\t\tJUEGO DE LOS ESPEJOS")
        print("El Juego de los Espejos podría ser un videojuego o simulador basado en la lógica y el reflejo de imágenes en espejos.")
        print("El objetivo podría ser guiar un rayo de luz o un objeto a través de un laberinto usando espejos, teniendo en cuenta las")
        print("reflexiones, ángulos y obstáculos que podrían estar presentes.")
        print("\t\t\t\tNivel de Prueba")
        self.matriz.mostrar_tablero()
