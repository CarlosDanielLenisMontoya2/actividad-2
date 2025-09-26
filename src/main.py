# main.py - Motor de inferencia y búsqueda
from collections import deque
from reglas import conexiones

def mejor_ruta(inicio, destino):
    """
    Encuentra la mejor ruta entre inicio y destino usando búsqueda en anchura (BFS).
    """
    visitados = set()
    cola = deque([[inicio]])
    
    while cola:
        ruta = cola.popleft()
        nodo = ruta[-1]
        
        if nodo == destino:
            return ruta
        
        if nodo not in visitados:
            for vecino in conexiones.get(nodo, []):
                nueva_ruta = list(ruta)
                nueva_ruta.append(vecino)
                cola.append(nueva_ruta)
            visitados.add(nodo)
    
    return None


if __name__ == "__main__":
    print("=== Sistema Inteligente de Rutas ===")
    inicio = input("Ingrese estación de inicio: ").strip().upper()
    destino = input("Ingrese estación de destino: ").strip().upper()
    
    ruta = mejor_ruta(inicio, destino)
    
    if ruta:
        print(f"La mejor ruta de {inicio} a {destino} es: {ruta}")
    else:
        print("No hay ruta disponible entre las estaciones ingresadas.")
