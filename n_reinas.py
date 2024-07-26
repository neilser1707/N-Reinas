n = 16 #Disfute poniendo 16 reinas en un tablero de 16x16 :)
total = 0

def es_valido(tablero, row, col):
    # Revisar si se puede colocar en esa fila
    for i in range(col):
        if tablero[row][i]:
            print("Falso 1")
            return False
        
    # Revisar la diagonal superior izquierda
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if tablero[i][j]:
            print("Falso 2")
            return False
        
    # Revisar la diagonal inferior izquierda
    for i, j in zip(range(row+1, n), range(col-1, -1, -1)):
        if tablero[i][j]:
            print("Falso 3")
            return False
    print("Verdadero")
    return True

def ubica_reinas(tablero, col):
    global total
    if col == n:
        total += 1  # Incrementa el total cuando se encuentra una solución
        return 1
    for row in range(n):
        if es_valido(tablero, row, col):
            tablero[row][col] = True
            ubica_reinas(tablero, col + 1)
            tablero[row][col] = False  # Retrocede
    return total

def n_reinas(n):
    # Inicializa el tablero como una lista de listas con valores False
    tablero = [[False for _ in range(n)] for _ in range(n)]
    resultado = ubica_reinas(tablero, 0)
    print(f"Total de soluciones para {n} reinas en un tablero de {n} x {n} : {resultado}")

n_reinas(n)