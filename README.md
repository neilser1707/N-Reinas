# N-Reinas
El problema de las n-reinas, inicialmente planteado para 8 reinas en un típico tablero de ajedrez, es un problema al cual se le puede dar solución utilizando backtracking
>El problema consiste en hallar el número máximo de posibles posiciones en las cuales n reinas puedan colocarse en un tablero de nxn sin que estás se amenacen

### Pasos que recorre el algoritmo:
* **Coloca una reina**
* **Si esta no se encuentra en amenaza continúa a la siguiente fila**
* **Si esta se encuentra en amenaza continúa buscando una posición válida**
* **Al terminar de ubicar a las reinas, cuenta esta opcion como una opción válida**
* **Repite el proceso comenzando ahora por la siguiente posición a la inicial de la ocasión pasada**

#### **Tabla de contenido:**
* **Instalación**
* **Uso**
* **Características**
* **Contribución**
* **Licencia**

#### Instalación
>1. Clonar el repositorio: git clone
>2. Crea y activa un entorno virtual: pipenv install - pipenv shell

#### Uso
>1. Ejecuta el script **n_reinas**: python n_reinas.py

#### Características
>1. Es un pequeño script con fines educativos 
>2. Utiliza backtracking y recursividad para hallar la solución

