import networkx as nx
import pandas as pd
import math

def construir_grafo(caminho_distancias='data/matriz_distancias.csv'):
    dist_matrix = pd.read_csv(caminho_distancias, index_col=0, header=0)
    dist_matrix.index = dist_matrix.index.astype(str)
    dist_matrix.columns = dist_matrix.columns.astype(str)
    dist_matrix = dist_matrix.apply(pd.to_numeric, errors='coerce')

    G = nx.Graph()
    for i in dist_matrix.index:
        for j in dist_matrix.columns:
            if i == j:
                continue
            valor = pd.to_numeric(dist_matrix.at[i, j], errors='coerce')
            if pd.isna(valor):
                continue
            G.add_edge(i, j, weight=float(valor))
    return G


def heuristica_euclidiana(u, v, posicoes):
    lat1, lon1 = posicoes[u]
    lat2, lon2 = posicoes[v]
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)


def encontrar_rota(grafo, origem, destino, posicoes=None):
    """
    Encontra a rota ótima entre origem e destino.
    Usa A* se posicoes for passado, senão Dijkstra.
    """
    if posicoes:
        h = lambda a, b: heuristica_euclidiana(a, b, posicoes)
        return nx.astar_path(grafo, source=origem, target=destino, heuristic=h, weight='weight')
    else:
        return nx.shortest_path(grafo, source=origem, target=destino, weight='weight')
