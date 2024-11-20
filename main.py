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
    
    # Configurar el nivel
    juego.configurar_nivel_personalizado(
        pos_luz=config_mapa['luz_pos'],
        dir_luz=config_mapa['luz_dir'],
        pos_meta=config_mapa['meta_pos'],
        obstaculos=config_mapa['obstaculos']
    )
    
    # Mostrar descripción del nivel
    print(config_mapa['descripcion'])
    input("Presione Enter para comenzar...")

    while True:
        juego.mostrar_tablero()
        print("\nOpciones:")
        print("1. Colocar espejo")
        print("2. Eliminar espejo")
        print("3. Simular trayectoria de luz")
        print("4. Ver historial")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            try:
                x = int(input("Ingrese posición X: "))
                y = int(input("Ingrese posición Y: "))
                print("\nTipos de espejo:")
                print("1: Diagonal (/)   2: Diagonal (\\)")
                print("3: Horizontal (─)  4: Vertical (│)")
                tipo = int(input("Seleccione tipo de espejo: "))
                if tipo not in [1, 2, 3, 4]:
                    print("Tipo de espejo inválido")
                    continue
                    
                exito, mensaje = juego.colocar_espejo(x, y, tipo)
                print(mensaje)
            except ValueError:
                print("Entrada inválida")

        elif opcion == "2":
            try:
                 x = int(input("Ingrese posición X del espejo a eliminar: "))
                 y = int(input("Ingrese posición Y del espejo a eliminar: "))
                 exito, mensaje = juego.eliminar_espejo(x, y)
                 print(mensaje)
            except ValueError:
                print("Entrada inválida")
            
                
        elif opcion == "3":
            juego.simular_luz()
            input("\nPresione Enter para continuar...")
            
        elif opcion == "4":
            juego.mostrar_historial()
            input("\nPresione Enter para continuar...")
            
        elif opcion == "5":
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()
