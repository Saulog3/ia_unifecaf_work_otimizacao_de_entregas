from flask import Flask, render_template, request
import pandas as pd
import folium
from src.clustering import clusterizar_entregas
from src.graph import construir_grafo, encontrar_rota

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Clusterizar entregas
        dados = clusterizar_entregas()

        # Construir grafo e encontrar rota de exemplo
        grafo = construir_grafo()
        rota = encontrar_rota(grafo, 'P5', 'P10')  # Exemplo: restaurante P5 para cliente P10

        # Plotar mapa
        mapa = folium.Map(location=[23.55, 46.65], zoom_start=12)
        for _, row in dados.iterrows():
            color = 'red' if row['tipo'] == 'restaurante' else 'blue'
            folium.CircleMarker(
                location=[row["lat"], row["lon"]],
                radius=5,
                color=color,
                fill=True,
                fill_color=color,
                popup=f"{row['id']} (Cluster {row['cluster']})"
            ).add_to(mapa)

        # Salvar mapa
        mapa.save('static/cluster_plot.html')

        return render_template('resultado.html', rota=rota)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
