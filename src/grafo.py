import heapq

class Graph:
    def __init__(self):
        self.nodes = {}
    
    def add_edge(self, origem, destino, distancia):
        self.nodes.setdefault(origem, []).append((destino, distancia))
        self.nodes.setdefault(destino, []).append((origem, distancia))

    def gerar_exemplo(self):
        # Grafo simplificado de bairros
        self.add_edge('A', 'B', 3)
        self.add_edge('A', 'C', 2)
        self.add_edge('B', 'D', 4)
        self.add_edge('C', 'D', 1)
        self.add_edge('D', 'E', 5)

    def heuristica(self, no, destino):
        # Heurística simples (pode ser adaptada)
        return abs(ord(destino) - ord(no))

    def a_star(self, inicio, fim):
        fila = [(0, inicio, [])]
        visitados = set()

        while fila:
            (custo, no, caminho) = heapq.heappop(fila)
            if no in visitados:
                continue
            caminho = caminho + [no]
            visitados.add(no)

            if no == fim:
                return caminho

            for vizinho, dist in self.nodes.get(no, []):
                if vizinho not in visitados:
                    prioridade = custo + dist + self.heuristica(vizinho, fim)
                    heapq.heappush(fila, (prioridade, vizinho, caminho))
        return None