import time
import os
from collections import deque

class TipoObjeto:
    VACIO = " "
    OBSTACULO = "■"  # Obstáculo oculto
    ESPEJO_DIAGONAL1 = "/"
    ESPEJO_DIAGONAL2 = "\\"
    ESPEJO_HORIZONTAL = "─"
    ESPEJO_VERTICAL = "│"
    LUZ = "☀"
    META = "★"

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
        self.pos_meta = (tamano-1, tamano-1)
        self.configurar_nivel()

    def configurar_nivel(self):
        # Colocar luz inicial
        self.tablero[self.pos_luz[0]][self.pos_luz[1]] = TipoObjeto.LUZ
        
        # Colocar meta
        self.tablero[self.pos_meta[0]][self.pos_meta[1]] = TipoObjeto.META
        
        # Colocar obstáculos aleatorios (ocultos)
        import random
        num_obstaculos = self.tamano // 2
        for _ in range(num_obstaculos):
            x, y = random.randint(1, self.tamano-2), random.randint(1, self.tamano-2)
            if (x, y) != self.pos_luz and (x, y) != self.pos_meta:
                self.tablero_oculto[x][y] = TipoObjeto.OBSTACULO

    def mostrar_tablero(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nEje X →")
        print("    " + " ".join([f"{i:2}" for i in range(self.tamano)]))
        print("   " + "─" * (self.tamano * 3 + 1))
        for i in range(self.tamano):
            print(f"Y{i:2}│", end=" ")
            for j in range(self.tamano):
                print(f"{self.tablero[i][j]:2}", end=" ")
            print()
        print()

    def colocar_espejo(self, x, y, tipo):
        if not (0 <= y < self.tamano and 0 <= x < self.tamano):
            return False, "Posición fuera del tablero"
        
        if self.tablero[y][x] != TipoObjeto.VACIO:
            return False, "Posición ocupada"

        simbolos = {
            1: TipoObjeto.ESPEJO_DIAGONAL1,
            2: TipoObjeto.ESPEJO_DIAGONAL2,
            3: TipoObjeto.ESPEJO_HORIZONTAL,
            4: TipoObjeto.ESPEJO_VERTICAL
        }
        
        self.tablero[y][x] = simbolos[tipo]
        self.historial.append(Accion(tipo, x, y))
        return True, "Espejo colocado exitosamente"


    def eliminar_espejo(self, x, y):
        if not (0 <= y < self.tamano and 0 <= x < self.tamano):
            return False, "Posición fuera del tablero"

        tipo_espejo = self.tablero[y][x]
        tipo_numerico = {
            TipoObjeto.ESPEJO_DIAGONAL1: 1,
            TipoObjeto.ESPEJO_DIAGONAL2: 2,
            TipoObjeto.ESPEJO_HORIZONTAL: 3,
            TipoObjeto.ESPEJO_VERTICAL: 4
        }.get(tipo_espejo, None)

        if tipo_numerico is None:
            return False, "No hay un espejo en esa posición"

        # Eliminar el espejo y agregar al historial
        self.tablero[y][x] = TipoObjeto.VACIO
        self.historial.append(f"[{time.strftime('%H:%M:%S')}] Eliminado espejo tipo {tipo_numerico} de ({x}, {y})")
        return True, "Espejo eliminado exitosamente"


    
    def simular_luz(self):
        x, y = self.pos_luz
        dx, dy = self.dir_luz
        camino = [(x, y)]

        while True:
            nuevo_x, nuevo_y = x + dx, y + dy

            # Verificar límites del tablero
            if not (0 <= nuevo_x < self.tamano and 0 <= nuevo_y < self.tamano):
                print("¡La luz llegó al límite del tablero!")
                break

            # Verificar obstáculos ocultos
            if self.tablero_oculto[nuevo_x][nuevo_y] == TipoObjeto.OBSTACULO:
                print("¡La luz chocó con un obstáculo oculto! Intenta de nuevo.")
                return False

            # Verificar meta
            if (nuevo_x, nuevo_y) == self.pos_meta:
                self.revelar_obstaculos()  # Revelar los obstáculos al ganar
                return True

            # Verificar espejos y actualizar dirección
            celda = self.tablero[nuevo_x][nuevo_y]
            if celda in [TipoObjeto.ESPEJO_DIAGONAL1, TipoObjeto.ESPEJO_DIAGONAL2,
                         TipoObjeto.ESPEJO_HORIZONTAL, TipoObjeto.ESPEJO_VERTICAL]:
                if celda == TipoObjeto.ESPEJO_DIAGONAL1:    # /
                    dx, dy = -dy, -dx
                elif celda == TipoObjeto.ESPEJO_DIAGONAL2:  # \
                    dx, dy = dy, dx
                elif celda == TipoObjeto.ESPEJO_HORIZONTAL: # ─
                    dx = -dx
                elif celda == TipoObjeto.ESPEJO_VERTICAL:   # │
                    dy = -dy

            x, y = nuevo_x, nuevo_y
            camino.append((x, y))

            # Visualizar el movimiento
            self.mostrar_movimiento(camino)
            time.sleep(0.5)


    def revelar_obstaculos(self):
        for i in range(self.tamano):
            for j in range(self.tamano):
                if self.tablero_oculto[i][j] == TipoObjeto.OBSTACULO:
                    self.tablero[i][j] = TipoObjeto.OBSTACULO
        self.mostrar_tablero()
        print("¡Felicitaciones! ¡Has alcanzado la meta y todos los obstáculos han sido revelados!")


    def mostrar_movimiento(self, camino):
        tablero_temp = [fila[:] for fila in self.tablero]
        for x, y in camino[:-1]:
            if tablero_temp[x][y] == TipoObjeto.LUZ:
                tablero_temp[x][y] = "·"
        x, y = camino[-1]
        tablero_temp[x][y] = TipoObjeto.LUZ
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n  " + " ".join([f"{i:2}" for i in range(self.tamano)]))
        for i in range(self.tamano):
            print(f"{i:2}", end=" ")
            for j in range(self.tamano):
                print(f"{tablero_temp[i][j]:2}", end=" ")
            print()
        print()

    def mostrar_historial(self):
        print("\nHistorial de acciones:")
        for accion in self.historial:
            print(accion)

    def configurar_nivel_personalizado(self, pos_luz, dir_luz, pos_meta, obstaculos):
        # Reiniciar tablero
        self.tablero = [[TipoObjeto.VACIO] * self.tamano for _ in range(self.tamano)]
        self.tablero_oculto = [[TipoObjeto.VACIO] * self.tamano for _ in range(self.tamano)]
        
        # Configurar posición inicial de la luz
        self.pos_luz = pos_luz
        self.dir_luz = dir_luz
        self.tablero[pos_luz[0]][pos_luz[1]] = TipoObjeto.LUZ
        
        # Configurar meta
        self.pos_meta = pos_meta
        self.tablero[pos_meta[0]][pos_meta[1]] = TipoObjeto.META
        
        # Colocar obstáculos
        for obs_y, obs_x in obstaculos:
            self.tablero_oculto[obs_y][obs_x] = TipoObjeto.OBSTACULO
