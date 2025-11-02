# src/optimizer.py
import argparse
from graph import load_graph
from clustering import cluster_orders, plot_clusters
from routing import a_star
import networkx as nx
import matplotlib.pyplot as plt

def assign_and_route(map_nodes, map_edges, orders_csv, k, out):
    G = load_graph(map_nodes, map_edges)
    df, kmeans = cluster_orders(orders_csv, k=k)
    plot_clusters(df, kmeans, out + '_clusters.png')

    # for each cluster: map order coords to nearest graph node, then TSP-ish route:
    results = {}
    for c in df['cluster'].unique():
        sub = df[df['cluster']==c]
        # map to nearest node
        nodes = list(G.nodes())
        # naive nearest mapping:
        order_nodes = []
        for _, row in sub.iterrows():
            best=None; bestd=1e12
            for n in nodes:
                d = ((row.lat-G.nodes[n]['lat'])**2 + (row.lon-G.nodes[n]['lon'])**2)**0.5
                if d<bestd: best=n; bestd=d
            order_nodes.append(best)
        # simple route: start from restaurant node 0 (assume 1) and do greedy nearest
        route=[1]  # substitute pelo id real do restaurante
        remaining = set(order_nodes)
        cur = route[-1]
        while remaining:
            nxt = min(remaining, key=lambda x: nx.shortest_path_length(G, cur, x, weight='dist_m'))
            path, dist = a_star(G, cur, nxt)
            route += path[1:]
            cur = nxt
            remaining.remove(nxt)
        results[c]=route

    # desenhar rotas sobre grafo (simplificado)
    plt.figure(figsize=(8,8))
    pos = {n:(G.nodes[n]['lon'], G.nodes[n]['lat']) for n in G.nodes()}
    nx.draw(G, pos, node_size=10, alpha=0.3)
    for r in results.values():
        edges = list(zip(r, r[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=r, node_size=20)
        nx.draw_networkx_edges(G, pos, edgelist=edges, width=2)
    plt.savefig(out + '_routes.png', dpi=150)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--map_nodes', required=True)
    parser.add_argument('--map_edges', required=True)
    parser.add_argument('--orders', required=True)
    parser.add_argument('--k', type=int, default=3)
    parser.add_argument('--out', default='outputs/run1')
    args = parser.parse_args()
    assign_and_route(args.map_nodes, args.map_edges, args.orders, args.k, args.out)