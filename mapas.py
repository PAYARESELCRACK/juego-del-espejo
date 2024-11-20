class Mapas:
    @staticmethod
    def obtener_mapa(numero_mapa):
        mapas = {
            1: {
                'tamano': 8,
                'luz_pos': (0, 0),      # Posición inicial de la luz (y, x)
                'luz_dir': (1, 0),      # Dirección inicial de la luz (abajo)
                'meta_pos': (7, 7),     # Posición de la meta (y, x)
                'obstaculos': [         # Lista de obstáculos (y, x)
                    (2, 3),
                    (2, 4),
                    (3, 3),
                    (4, 5),
                    (5, 5),
                    (5, 2)
                ],
                'descripcion': """
                Nivel 1: El Camino Básico
                Objetivo: Guía la luz desde la esquina superior izquierda 
                hasta la esquina inferior derecha evitando los obstáculos.
                Dificultad: Fácil
                """
            },
            2: {
                'tamano': 10,
                'luz_pos': (0, 5),      # Luz comienza en el centro superior
                'luz_dir': (1, 0),      # Dirección inicial hacia abajo
                'meta_pos': (9, 5),     # Meta en el centro inferior
                'obstaculos': [         # Patrón de obstáculos más complejo
                    (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),  # Barrera horizontal
                    (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),  # Segunda barrera
                    (4, 1), (5, 1),                          # Obstáculos laterales
                    (4, 8), (5, 8)
                ],
                'descripcion': """
                Nivel 2: El Laberinto
                Objetivo: Navega a través de las barreras de obstáculos 
                para llegar a la meta. Necesitarás usar múltiples espejos 
                y reflexiones para completar este nivel.
                Dificultad: Medio
                """
            }
        }
        
        return mapas.get(numero_mapa, None)

    @staticmethod
    def listar_mapas():
        print("\nMapas disponibles:")
        print("1. El Camino Básico - Un nivel introductorio para aprender los conceptos básicos")
        print("2. El Laberinto - Un desafío más complejo con múltiples obstáculos")
