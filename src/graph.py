import networkx as nx
import pandas as pd

def construir_grafo(caminho_distancias='data/matriz_distancias.csv'):
    """
    Constrói um grafo a partir da matriz de distâncias.
    """
    dist_matrix = pd.read_csv(caminho_distancias, index_col=0)
    G = nx.Graph()
    for i in dist_matrix.index:
        for j in dist_matrix.columns:
            G.add_edge(i, j, weight=dist_matrix.loc[i, j])
    return G

def encontrar_rota(grafo, origem, destino):
    """
    Encontra a rota ótima entre dois pontos usando A*.
    """
    return nx.astar_path(grafo, source=origem, target=destino, heuristic=lambda u, v: 0.01)
