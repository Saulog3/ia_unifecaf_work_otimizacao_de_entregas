import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import os

def agrupar_entregas(df):
    X = df[['x', 'y']].values
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['cluster'] = kmeans.fit_predict(X)

    plt.figure(figsize=(6, 4))
    plt.scatter(df['x'], df['y'], c=df['cluster'], cmap='viridis')
    plt.title('Agrupamento de Entregas (K-Means)')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    caminho_img = os.path.join('static', 'cluster_plot.png')
    plt.savefig(caminho_img)
    plt.close()

    return df.to_html(classes='table table-striped'), 'cluster_plot.png'