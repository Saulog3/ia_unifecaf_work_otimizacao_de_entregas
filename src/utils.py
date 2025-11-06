# src/utils.py
import folium
import pandas as pd
from folium import FeatureGroup

def gerar_mapa_com_rotas(dados, rotas_dict, caminho_saida='static/cluster_plot.html'):
    """
    dados: DataFrame com id, lat, lon, tipo, cluster
    rotas_dict: dict {nome_rota: [id1, id2, ...]}
    Gera um mapa com markers e PolyLines para cada rota.
    """
    mapa = folium.Map(location=[dados['lat'].mean(), dados['lon'].mean()], zoom_start=13)

    # grupos de camada por tipo
    pontos_fg = FeatureGroup(name='Pontos')
    for _, row in dados.iterrows():
        color = 'red' if row.get('tipo') == 'restaurante' else 'blue'
        folium.CircleMarker(
            location=[row['lat'], row['lon']],
            radius=5,
            color=color,
            fill=True,
            fill_color=color,
            popup=f"{row['id']} (Cluster {row['cluster']})"
        ).add_to(pontos_fg)
    pontos_fg.add_to(mapa)

    # desenhar rotas
    for nome, rota in rotas_dict.items():
        rota_coords = []
        for ponto in rota:
            p = dados.loc[dados['id'] == ponto, ['lat', 'lon']]
            if not p.empty:
                rota_coords.append((p.iloc[0]['lat'], p.iloc[0]['lon']))
        if rota_coords:
            folium.PolyLine(locations=rota_coords, tooltip=nome, weight=4, opacity=0.8).add_to(mapa)

    folium.LayerControl().add_to(mapa)
    mapa.save(caminho_saida)
    return caminho_saida
