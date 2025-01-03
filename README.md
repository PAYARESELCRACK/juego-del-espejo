JUEGO DE LOS ESPEJOS
Crear un "Juego de los Espejos" como un proyecto para Estructuras de Datos puede ser una forma interesante de aplicar conceptos como listas, 
pilas, colas, árboles, grafos o matrices. Aquí tienes algunas ideas para diseñar este juego en ese contexto:

Concepto Básico
El "Juego de los Espejos" podría ser un videojuego o simulador basado en la lógica y el reflejo de imágenes en espejos. 
El objetivo podría ser guiar un rayo de luz o un objeto a través de un laberinto usando espejos, teniendo en cuenta las reflexiones, 
ángulos y obstáculos que podrían estar presentes.

Posibles estructuras de datos a utilizar:
        *Matrices: El tablero del juego puede ser representado como una matriz 2D donde cada celda puede tener un objeto (espejo, obstáculo, 
        rayo de luz, vacío, etc.). Los espejos pueden cambiar la dirección del rayo según el ángulo de incidencia. Por ejemplo:
        [0, 0, E, O] → Representa una fila con un espejo (M) y un obstáculo (O).

        *Pila: Se utilizará la pila para implementar el historial de acciones para guiar al espejo
        *El rayo de luz se propaga en la matriz según las reglas de reflexión, la dirección del rayo va cambiar con base a las propiedades de direccion
        de cada objeto "espejo" o "obstaculo".

Características adicionales:
Niveles de dificultad: Los niveles podrían implicar tableros más grandes o complejos, con más obstáculos y espejos. 
También podrías incorporar temporizadores para agregar un componente de tiempo real. (opcional, creado todavia)

Objetivo: Pensar en la ruta para que la luz pueda llegar a la meta. La fuente de luz se encontrará en el centro del tablero y la mision del
jugador será colocar los espejos de tal manera que pueda crear una ruta para que el espejo pueda llegar a la meta, en el tablero existirán
obstaculos que, si la luz llegue a colisionar con un obstaculo, la luz se detendrá.

En el tablero existirá espacios vacios los que hará que la luz pueda salir del tablero, si no está en la meta, se reportará como si chocara La
luz, y se tendrá que reintentar.

Ejemplo: Tablero de 9x9
| |OB|OB| |OB| |OB| |OB|
| | |OB| | | | |OB |OB|
|OB| | | |E| | | |OB|
| | |E| | | | | | |
|OB| | | |L| | | |OB|
| | | | | | | | |OB|
|OB| |E| | | |E | |OB|
| | | | | | |E| |E|
|OB|OB|OB| |OB| |OB|ME|ME|
