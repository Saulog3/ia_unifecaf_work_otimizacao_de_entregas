# Sabor Express – Otimização Inteligente de Rotas de Entrega

## Projeto Acadêmico — Inteligência Artificial Aplicada

## Descrição do Problema

A empresa fictícia Sabor Express, que realiza entregas de alimentos na região central da cidade, enfrenta atrasos e custos elevados devido à definição manual das rotas pelos entregadores.

O objetivo é desenvolver uma solução baseada em Inteligência Artificial (IA) para agrupar e otimizar rotas de entregas próximas e sugerir as melhores rotas.

## Objetivos do Projeto

Implementar algoritmos de IA para otimização de rotas.

Representar o mapa da cidade como um grafo ponderado.

Aplicar clustering (K-Means) para agrupar pedidos por região.

Usar busca heurística (A*) e heurística TSP (2-opt) para otimizar rotas dentro de cada cluster.

Visualizar as entregas e rotas em um mapa interativo (Folium).

## Algoritmos e Conceitos Utilizados

| Tipo                           | Algoritmo                      | Aplicação                                |
| ------------------------------ | ------------------------------ | ---------------------------------------- |
| Aprendizado não supervisionado | **K-Means**                    | Agrupamento de entregas próximas         |
| Busca heurística               | **A*** (A-Star)                | Menor caminho entre dois pontos no grafo |
| Otimização local               | **2-opt (TSP Heurístico)**     | Rota ótima dentro de cada cluster        |
| Estrutura de dados             | **Grafo ponderado (NetworkX)** | Representação das conexões entre locais  |
| Visualização geográfica        | **Folium**                     | Mapa interativo com clusters e rotas     |


dados -> clusterização (K-Means)
      -> construção de grafo (NetworkX)
      -> otimização de rotas (A* / 2-opt)
      -> visualização no mapa (Folium)


## Principais Módulos

clustering.py

Aplica K-Means sobre coordenadas (lat, lon).

Lida com valores ausentes via imputação da média.

Define automaticamente o número ideal de clusters via Silhouette Score.

graph.py

Constrói o grafo de distâncias a partir de uma matriz CSV.

Implementa o algoritmo A* com heurística de distância geográfica.

Pode usar Dijkstra como fallback (quando sem heurística).

routing.py

Implementa 2-opt, uma heurística eficiente para o Problema do Caixeiro Viajante (TSP).

Otimiza a rota interna de cada cluster (cada entregador cobre um cluster).

utils.py

Gera mapas interativos com Folium.

Exibe clusters, pontos e rotas com cores e tooltips informativos.