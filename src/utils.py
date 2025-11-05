import folium
import pandas as pd

dados = pd.read_csv('../data/entregas_clusterizadas.csv')
mapa = folium.Map(location=[23.55, 46.65], zoom_start=12)
for _, row in dados.iterrows():
    color = 'red' if row['tipo'] == 'restaurante' else 'blue'
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=5,
        color=color,
        fill=True,
        fill_color=color,
        popup=f"{row['id']} (Cluster {row['cluster']})"
    ).add_to(mapa)
mapa.save('../static/cluster_plot.html')
