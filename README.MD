# Sabor Express – Otimização Inteligente de Rotas de Entrega

###  Projeto Acadêmico — Inteligência Artificial Aplicada

---

## Descrição do Problema

A empresa fictícia **Sabor Express**, que realiza entregas de alimentos na região central da cidade, enfrenta atrasos e custos elevados devido à **definição manual das rotas** pelos entregadores.  

O objetivo deste projeto é desenvolver uma **solução baseada em Inteligência Artificial (IA)** capaz de **agrupar entregas próximas** e **sugerir as melhores rotas de entrega**, reduzindo tempo e distância percorrida.

---

## Objetivos do Projeto

- Implementar algoritmos de **IA clássicos** para otimização de rotas.  
- Representar o mapa da cidade como um **grafo ponderado**.  
- Aplicar **clustering (K-Means)** para agrupar pedidos por região.  
- Usar **busca heurística (A*)** e **heurística TSP (2-opt)** para otimizar rotas dentro de cada cluster.  
- Visualizar as entregas e rotas em um **mapa interativo (Folium)**.  

---

## Algoritmos e Conceitos Utilizados

| Tipo | Algoritmo | Aplicação |
|------|------------|-----------|
| Aprendizado não supervisionado | **K-Means** | Agrupamento de entregas próximas |
| Busca heurística | **A*** (A-Star) | Menor caminho entre dois pontos no grafo |
| Otimização local | **2-opt (TSP Heurístico)** | Rota ótima dentro de cada cluster |
| Estrutura de dados | **Grafo ponderado (NetworkX)** | Representação das conexões entre locais |
| Visualização geográfica | **Folium** | Mapa interativo com clusters e rotas |

---

##  Arquitetura e Fluxo da Solução

```
dados -> clusterização (K-Means)
      -> construção de grafo (NetworkX)
      -> otimização de rotas (A* / 2-opt)
      -> visualização no mapa (Folium)
```

### Estrutura de Pastas

```
sabor-express/
├─ app.py
├─ src/
│  ├─ __init__.py
│  ├─ clustering.py
│  ├─ graph.py
│  ├─ routing.py
│  └─ utils.py
├─ data/
│  ├─ pontos_entrega.csv
│  ├─ matriz_distancias.csv
│  └─ entregas_clusterizadas.csv
├─ templates/
│  ├─ index.html
│  └─ resultado.html
├─ static/
│  ├─ style.css
│  └─ cluster_plot.html
└─ README.md
```

---

## Principais Módulos

### `clustering.py`
- Aplica **K-Means** sobre coordenadas (lat, lon).
- Lida com valores ausentes via imputação da média.
- Define automaticamente o número ideal de clusters via **Silhouette Score**.

### `graph.py`
- Constrói o **grafo de distâncias** a partir de uma matriz CSV.
- Implementa o algoritmo **A*** com heurística de distância geográfica.
- Pode usar Dijkstra como fallback (quando sem heurística).

### `routing.py`
- Implementa **2-opt**, uma heurística eficiente para o **Problema do Caixeiro Viajante (TSP)**.
- Otimiza a rota interna de cada cluster (cada entregador cobre um cluster).

### `utils.py`
- Gera **mapas interativos** com Folium.
- Exibe clusters, pontos e rotas com cores e tooltips informativos.

---

## Execução do Projeto

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Estrutura esperada de dados
Arquivo `data/pontos_entrega.csv` (exemplo):
```csv
id,lat,lon,tipo
R1,-23.5530,-46.6313,restaurante
C1,-23.5400,-46.6230,cliente
C2,-23.5650,-46.6400,cliente
```

### 3. Rodar o servidor Flask
```bash
python app.py
```

Acesse no navegador:
```
http://127.0.0.1:5000
```

---

## Visualização

O sistema gera automaticamente o arquivo:
```
static/cluster_plot.html
```

Visualize no navegador para ver:
- Pontos de entrega coloridos por cluster.
- Linhas de rota otimizadas (em verde).
- Popup com identificador e tipo de ponto.

---

## Métricas e Avaliação

| Métrica | Descrição | Resultado esperado |
|----------|------------|--------------------|
| **Silhouette Score** | Qualidade dos clusters | > 0.5 (bom agrupamento) |
| **Distância total percorrida** | Soma das arestas percorridas por entregador | Redução em relação à rota manual |
| **Tempo estimado** | Baseado em velocidade média (km/h) | Redução de ~20–30% |
| **Número de clusters** | Determinado automaticamente | Balanceado entre entregadores |

---

## Resultados Observados

- O agrupamento via **K-Means** reduziu a sobreposição de áreas de entrega.  
- O algoritmo **A*** encontrou rotas eficientes com custo menor.  
- A heurística **2-opt** melhorou a rota em cada cluster, reduzindo a distância total.  
- A visualização no Folium facilitou a interpretação e análise das zonas de entrega.

---

## Limitações e Melhorias Futuras

| Limitação | Possível melhoria |
|------------|------------------|
| Distâncias estáticas | Integrar dados de tráfego em tempo real |
| Heurística simples | Testar algoritmos genéticos ou MILP |
| TSP local por cluster | Implementar metaheurísticas globais (Simulated Annealing, RL) |
| Dados sintéticos | Integrar API de mapas reais (Google Maps / OpenRouteService) |

---

## Referências e Inspirações

1. **UPS ORION** – *On-Road Integrated Optimization and Navigation*  
   - Case real de otimização logística com heurísticas + dados em tempo real.  
   - Fontes: *wired.com*, *jsaer.com*

2. **Medium – “Optimizing Logistics: Clustering e MILP”**  
   - Aplicação prática de K-Means + Programação Linear Inteira Mista.  
   - Fonte: *medium.com*

3. **ResearchGate – “AI-Powered Route Optimization”**  
   - Integração de IA e algoritmos heurísticos em logística.  
   - Fonte: *researchgate.net*

4. **Kardinal.ai – Case “Fresh Product Delivery”**  
   - Planejamento dinâmico e análise territorial em entregas de perecíveis.  

---

## Autoria

**Saulo Cunha**  
📘 Projeto desenvolvido como parte da disciplina **Artificial Intelligence Fundamentals**  
 Tema: *IA aplicada à otimização de rotas de entrega (clustering + busca heurística)*  

---


## Exemplo de resultado

![Mapa de entregas com clusters e rotas](static/Resultados_Rotas.png)


---

### Conclusão

> A aplicação desenvolvida demonstra como **técnicas clássicas de IA (K-Means, A*) podem gerar ganhos reais em eficiência logística**, reduzindo custos e tempo de entrega — exatamente o tipo de valor que sistemas como o **UPS ORION** trouxeram para a indústria.
