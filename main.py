import apoyo as ap
from mapas import Mapas

def main():
    # Mostrar mapas disponibles
    Mapas.listar_mapas()

    while True:
        try:
            nivel = int(input("\nSeleccione un nivel (1-2): "))
            if nivel not in [1, 2]:
                print("Por favor seleccione un nivel válido")
                continue
            break
        except ValueError:
            print("Por favor ingrese un número válido")

    # Obtener configuración del mapa
    config_mapa = Mapas.obtener_mapa(nivel)

    # Crear instancia del juego con la configuración del mapa
    juego = ap.Juego(tamano=config_mapa['tamano'])
    juego.configurar_nivel_personalizado(
        pos_luz=(0, 0),
        dir_luz=(1, 0),
        espejos_ocultos=config_mapa['obstaculos']
    )

    # Mostrar descripción del nivel
    print(config_mapa['descripcion'])
    input("Presione Enter para comenzar...")

    while True:
        juego.mostrar_tablero()
        print("\nOpciones:")
        print("1. Colocar marca (X)")
        print("2. Eliminar marca")
        print("3. Simular trayectoria de luz")
        print("4. Finalizar partida")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":  # Colocar marca
            if juego.marcas_restantes > 0:
                try:
                    x = int(input("Ingrese posición X: "))
                    y = int(input("Ingrese posición Y: "))
                    exito, mensaje = juego.colocar_marca(x, y)
                    print(mensaje)
                except ValueError:
                    print("Entrada inválida")
            else:
                print("No te quedan marcas disponibles.")

        elif opcion == "2":  # Eliminar marca
            try:
                x = int(input("Ingrese posición X de la marca a eliminar: "))
                y = int(input("Ingrese posición Y de la marca a eliminar: "))
                exito, mensaje = juego.eliminar_marca(x, y)
                print(mensaje)
            except ValueError:
                print("Entrada inválida")

        elif opcion == "3":  # Simular trayectoria de luz
            juego.simular_luz()
            input("\nPresione Enter para continuar...")

        elif opcion == "4":  # Finalizar partida
            juego.finalizar_partida()
            break

        elif opcion == "5":  # Salir del juego
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()
