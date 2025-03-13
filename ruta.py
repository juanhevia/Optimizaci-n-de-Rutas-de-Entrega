import heapq

class Nodo:
    def __init__(self, nombre, costo=0):
        self.nombre = nombre
        self.costo = costo
        self.adjacentes = []

    def agregar_adjacente(self, nodo, costo):
        self.adjacentes.append((nodo, costo))


class ArbolRutas:
    def __init__(self, raiz):
        self.raiz = raiz

    def mejor_ruta(self, origen, destino):
        # Usamos Dijkstra para encontrar el camino más corto entre origen y destino.
        # Usamos un heap (prioridad) para manejar los costos de manera eficiente.
        heap = [(0, origen)]  # (costo, nodo)
        visitados = set()
        costos = {origen: 0}
        camino = {origen: None}

        while heap:
            costo_actual, nodo_actual = heapq.heappop(heap)

            if nodo_actual in visitados:
                continue

            visitados.add(nodo_actual)

            if nodo_actual == destino:
                # Reconstruir el camino
                ruta = []
                while nodo_actual is not None:
                    ruta.append(nodo_actual.nombre)
                    nodo_actual = camino[nodo_actual]
                return ruta[::-1], costo_actual  # Devuelve el camino y el costo total

            for vecino, costo in nodo_actual.adjacentes:
                if vecino in visitados:
                    continue
                nuevo_costo = costo_actual + costo
                if vecino not in costos or nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    camino[vecino] = nodo_actual
                    heapq.heappush(heap, (nuevo_costo, vecino))

        return None, float('inf')  # Si no hay camino


# Crear los nodos (puntos de entrega)
origen = Nodo("Almacén")
a = Nodo("Punto A")
b = Nodo("Punto B")
c = Nodo("Punto C")
destino = Nodo("Punto D")

# Crear las rutas entre los nodos con sus costos (distancia o tiempo)
origen.agregar_adjacente(a, 10)
origen.agregar_adjacente(b, 15)
a.agregar_adjacente(c, 10)
b.agregar_adjacente(c, 5)
c.agregar_adjacente(destino, 5)

# Crear el árbol de rutas
arbol_rutas = ArbolRutas(origen)

# Buscar la mejor ruta de entrega
ruta, costo = arbol_rutas.mejor_ruta(origen, destino)

if ruta:
    print(f"La mejor ruta es: {' -> '.join([nodo.nombre for nodo in ruta])} con un costo total de {costo}")
else:
    print("No hay ruta disponible.")

