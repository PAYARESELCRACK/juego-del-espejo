import time
import os
from collections import deque

class TipoObjeto:
    VACIO = " "
    ESPEJO_INVISIBLE1 = "/"  # Espejo oculto diagonal /
    ESPEJO_INVISIBLE2 = "\\"  # Espejo oculto diagonal \
    ESPEJO_DIAGONAL1 = "/"
    ESPEJO_DIAGONAL2 = "\\"
    LUZ = "↓"  # Cambiado a flecha hacia abajo

class Accion:
    def __init__(self, tipo_espejo, x, y):
        self.tipo_espejo = tipo_espejo
        self.x = x
        self.y = y
        self.timestamp = time.strftime("%H:%M:%S")

    def __str__(self):
        return f"[{self.timestamp}] Colocado espejo tipo {self.tipo_espejo} en ({self.x}, {self.y})"

class Juego:
    def __init__(self, tamano=10):
        self.tamano = tamano
        self.tablero = [[TipoObjeto.VACIO] * tamano for _ in range(tamano)]
        self.tablero_oculto = [[TipoObjeto.VACIO] * tamano for _ in range(tamano)]
        self.historial = deque()
        self.pos_luz = (0, 0)
        self.dir_luz = (1, 0)  # Dirección inicial hacia abajo
        self.marcas_restantes = 15  # Máximo de marcas disponibles

    def simular_luz(self):
        """Simula la trayectoria del rayo interactuando con espejos visibles e invisibles."""
        x, y = self.pos_luz
        dx, dy = self.dir_luz
        print(f"Luz entra en ({y},{x})")

        while True:
            nuevo_x, nuevo_y = x + dx, y + dy
            # Verificar límites de salida
            if not (0 <= nuevo_x < self.tamano and 0 <= nuevo_y < self.tamano):
                salida_x = max(0, min(self.tamano - 1, nuevo_x))
                salida_y = max(0, min(self.tamano - 1, nuevo_y))
                print(f"Luz sale en ({salida_y},{salida_x})")
                break

            # Verificar interacción con espejos visibles e invisibles
            celda = self.tablero[nuevo_x][nuevo_y]
            espejo_oculto = self.tablero_oculto[nuevo_x][nuevo_y]

            # Comportamiento del rayo con espejos visibles
            if celda in [TipoObjeto.ESPEJO_DIAGONAL1, TipoObjeto.ESPEJO_DIAGONAL2]:
                if celda == TipoObjeto.ESPEJO_DIAGONAL1:
                    dx, dy = -dy, -dx
                elif celda == TipoObjeto.ESPEJO_DIAGONAL2:
                    dx, dy = dy, dx

            # Comportamiento del rayo con espejos invisibles
            elif espejo_oculto in [TipoObjeto.ESPEJO_INVISIBLE1, TipoObjeto.ESPEJO_INVISIBLE2]:
                if espejo_oculto == TipoObjeto.ESPEJO_INVISIBLE1:
                    dx, dy = -dy, -dx
                elif espejo_oculto == TipoObjeto.ESPEJO_INVISIBLE2:
                    dx, dy = dy, dx

            # Actualizar posición
            x, y = nuevo_x, nuevo_y



    def configurar_nivel_personalizado(self, pos_luz, dir_luz, espejos_ocultos):
        """Configura la posición inicial de la luz y los espejos invisibles."""
        # Configurar luz
        self.pos_luz = pos_luz
        self.dir_luz = dir_luz
        self.tablero[pos_luz[0]][pos_luz[1]] = TipoObjeto.LUZ

        # Colocar espejos invisibles en el tablero oculto
        for y, x in espejos_ocultos:
            tipo_espejo = TipoObjeto.ESPEJO_INVISIBLE1 if (y + x) % 2 == 0 else TipoObjeto.ESPEJO_INVISIBLE2
            self.tablero_oculto[y][x] = tipo_espejo

    def colocar_marca(self, x, y):
        """Coloca una marca (X) en el tablero."""
        if not (0 <= x < self.tamano and 0 <= y < self.tamano):
            return False, "Posición fuera del tablero."
        if self.tablero[y][x] != TipoObjeto.VACIO:
            return False, "Ya hay algo en esa posición."
        self.tablero[y][x] = "X"
        self.marcas_restantes -= 1
        return True, "Marca colocada exitosamente."

    def eliminar_marca(self, x, y):
        """Elimina una marca (X) del tablero."""
        if not (0 <= x < self.tamano and 0 <= y < self.tamano):
            return False, "Posición fuera del tablero."
        if self.tablero[y][x] != "X":
            return False, "No hay una marca en esa posición."
        self.tablero[y][x] = TipoObjeto.VACIO
        self.marcas_restantes += 1
        return True, "Marca eliminada exitosamente."

    def finalizar_partida(self):
        """Finaliza la partida, verifica las marcas y muestra el resultado."""
        # Compara las marcas con los espejos invisibles
        aciertos = 0
        total_espejos = sum(
            1 for y in range(self.tamano) for x in range(self.tamano)
            if self.tablero_oculto[y][x] in [TipoObjeto.ESPEJO_INVISIBLE1, TipoObjeto.ESPEJO_INVISIBLE2]
        )
        for y in range(self.tamano):
            for x in range(self.tamano):
                if self.tablero[y][x] == "X" and self.tablero_oculto[y][x] in [TipoObjeto.ESPEJO_INVISIBLE1, TipoObjeto.ESPEJO_INVISIBLE2]:
                    aciertos += 1

        # Animación final
        self.mostrar_animacion_final()

        # Determinar si ganó o perdió
        if aciertos == total_espejos:
            print("¡Felicidades! Has adivinado todos los espejos y ganado el juego.")
        else:
            print(f"¡Lo siento! Has perdido. Adivinaste correctamente {aciertos} de {total_espejos} espejos.")

        
        input("\nPresione Enter para salir..")
        return 



    def mostrar_animacion_final(self):
        """Muestra una animación alternando entre las marcas y los espejos ocultos."""
        import time
        for _ in range(9):  # 9 oscilaciones (0.5 segundos por estado, total ~9 segundos)
            # Mostrar tablero con marcas
            self.mostrar_tablero()
            time.sleep(0.5)

            # Mostrar tablero con espejos ocultos
            tablero_temp = [fila[:] for fila in self.tablero]  # Crear una copia temporal del tablero
            for y in range(self.tamano):
                for x in range(self.tamano):
                    if self.tablero_oculto[y][x] in [TipoObjeto.ESPEJO_INVISIBLE1, TipoObjeto.ESPEJO_INVISIBLE2]:
                        tablero_temp[y][x] = self.tablero_oculto[y][x]

            # Limpiar la pantalla antes de mostrar el nuevo estado
            os.system('cls' if os.name == 'nt' else 'clear')

            # Mostrar el tablero con los espejos ocultos (igual que la función mostrar_tablero)
            print("    ", end="")  
            for i in range(self.tamano):
                print(f"{i:2}", end=" ")  
            print()  

            # Borde superior del tablero
            print("   " + "─" * (self.tamano * 3 + 2))  # Asegura el borde superior correctamente alineado

            # Filas del tablero con los números del eje Y
            for y in range(self.tamano):
                print(f"{y:2} │", end=" ")  # Alineación de las coordenadas Y y borde izquierdo
                for x in range(self.tamano):
                    # Aseguramos que las celdas tengan el mismo ancho, usando `:2` para cada celda
                    print(f"{tablero_temp[y][x]:2}", end=" ")
                print("│")  # Borde derecho

            # Borde inferior del tablero
            print("   " + "─" * (self.tamano * 3 + 2))  # Borde inferior del tablero
            time.sleep(0.5)


    def mostrar_tablero(self):
        """Imprime el tablero cerrado con bordes y numeración de coordenadas."""
        os.system('cls' if os.name == 'nt' else 'clear')

       
        print("    ", end="")  
        for i in range(self.tamano):
            print(f"{i:2}", end=" ")  
        print()  

        # Borde superior del tablero
        print("   " + "─" * (self.tamano * 3 + 2))  # Asegura el borde superior correctamente alineado

        # Filas del tablero con los números del eje Y
        for y in range(self.tamano):
            print(f"{y:2} │", end=" ")  # Alineación de las coordenadas Y y borde izquierdo
            for x in range(self.tamano):
                # Aseguramos que las celdas tengan el mismo ancho, usando `:2` para cada celda
                print(f"{self.tablero[y][x]:2}", end=" ")
            print("│")  # Borde derecho

        # Borde inferior del tablero
        print("   " + "─" * (self.tamano * 3 + 2))  # Borde inferior del tablero


