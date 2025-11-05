import pandas as pd
from sklearn.cluster import KMeans



def clusterizar_entregas(caminho_entregas='data/pontos_entrega.csv', n_clusters=3):
    """
    Carrega os pontos de entrega, aplica K-Means e salva os clusters.
    """
    dados = pd.read_csv(caminho_entregas)
    X = dados[['lat', 'lon']]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(X)
    dados['cluster'] = kmeans.labels_
    dados.to_csv('data/entregas_clusterizadas.csv', index=False)
    return dados
