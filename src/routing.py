# src/routing.py
import math

def calcular_distancia_euclidiana(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def rota_total(coords, ordem):
    """soma das distâncias na ordem (lista de indices)"""
    total = 0.0
    for i in range(len(ordem)-1):
        total += calcular_distancia_euclidiana(coords[ordem[i]], coords[ordem[i+1]])
    return total

def two_opt(coords, ordem=None, max_iter=1000):
    """
    Simple 2-opt improvement for TSP. coords = list of (lat,lon).
    ordem = initial permutation (optional).
    Retorna nova ordem de indices.
    """
    n = len(coords)
    if ordem is None:
        ordem = list(range(n)) + [0]  # fechamento do ciclo
    best = ordem[:]
    improved = True
    it = 0
    while improved and it < max_iter:
        improved = False
        it += 1
        for i in range(1, n-1):
            for j in range(i+1, n):
                if j - i == 1: continue
                new_route = best[:i] + best[i:j][::-1] + best[j:]
                if rota_total(coords, new_route) < rota_total(coords, best):
                    best = new_route
                    improved = True
        # opcional: break se nenhuma melhora
    return best

def otimizar_rota_por_cluster(dados_cluster):
    """
    dados_cluster: DataFrame com colunas id, lat, lon.
    Retorna ordem otimizada de ids (ciclo fechado).
    """
    ids = list(dados_cluster['id'])
    coords = [(r['lat'], r['lon']) for _, r in dados_cluster.iterrows()]
    if len(coords) <= 2:
        return ids  # trivial

    ordem_idx = two_opt(coords)
    # converter indices para ids, removendo fechamento duplicado final se houver
    ordem_clean = [ids[i] for i in ordem_idx if i < len(ids)]
    return ordem_clean
