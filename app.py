# app.py
from flask import Flask, render_template, request
from src.clustering import clusterizar_entregas
from src.graph import construir_grafo, encontrar_rota
from src.routing import otimizar_rota_por_cluster
from src.utils import gerar_mapa_com_rotas
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # clusteriza (retorna df, modelo)
        dados, _ = clusterizar_entregas()

        # construir grafo (pode ser usado para rotas entre pares)
        grafo = construir_grafo()

        # preparar posicoes para heuristica (id -> (lat,lon))
        posicoes = {row['id']:(row['lat'], row['lon']) for _, row in dados.iterrows()}

        # Para cada cluster, otimizar rota interna via TSP 2-opt
        rotas_por_cluster = {}
        for cluster_id, dfc in dados.groupby('cluster'):
            dfc = dfc.reset_index(drop=True)
            if len(dfc) == 0: 
                continue
            ordem_ids = otimizar_rota_por_cluster(dfc)  # lista de ids
            rotas_por_cluster[f'Cluster {cluster_id}'] = ordem_ids

        # Exemplo adicional: rota entre um restaurante e um cliente (A*)
        # (substitua 'P5','P10' por ids válidos do seu data)
        exemplo_rota_astar = None
        try:
            exemplo_rota_astar = encontrar_rota(grafo, 'P5', 'P10', posicoes=posicoes)
        except Exception:
            exemplo_rota_astar = []

        # juntar rotas para visualização
        todas_rotas = {'TSP por cluster - '+k: v for k,v in rotas_por_cluster.items()}
        if exemplo_rota_astar:
            todas_rotas['Exemplo A* P5->P10'] = exemplo_rota_astar

        # gerar mapa com marcadores e rotas
        caminho_mapa = gerar_mapa_com_rotas(dados, todas_rotas)
        return render_template('resultado.html', mapa_path=caminho_mapa, rotas=todas_rotas)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
