import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.impute import SimpleImputer

def clusterizar_entregas(caminho_entregas='data/pontos_entrega.csv',
                         n_clusters=None,
                         caminho_saida='data/entregas_clusterizadas.csv',
                         random_state=42,
                         max_k=8):
    """
    Clusteriza pontos de entrega com KMeans, lidando com valores ausentes (NaN).
    """
    dados = pd.read_csv(caminho_entregas)
    if not {'lat', 'lon', 'id'}.issubset(dados.columns):
        raise ValueError("O CSV deve conter colunas: id, lat, lon")

    # Remove ou imputa valores ausentes
    imputer = SimpleImputer(strategy='mean')
    X = imputer.fit_transform(dados[['lat', 'lon']])

    # Escolha automática de clusters
    if n_clusters is None:
        best_k = 2
        best_score = -1
        for k in range(2, min(max_k, len(X))):
            model = KMeans(n_clusters=k, random_state=random_state).fit(X)
            try:
                score = silhouette_score(X, model.labels_)
            except Exception:
                score = -1
            if score > best_score:
                best_k = k
                best_score = score
        n_clusters = best_k

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state).fit(X)
    dados['cluster'] = kmeans.labels_
    dados.to_csv(caminho_saida, index=False)
    return dados, kmeans
