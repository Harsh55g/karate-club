import matplotlib
matplotlib.use('Agg')
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# Setup
G = nx.karate_club_graph()
A = nx.to_numpy_array(G, nodelist=sorted(G.nodes()))
n = G.number_of_nodes()
m = G.number_of_edges()
k = A.sum(axis=1)
k_col = k.reshape((n,1))
B = A - (k_col @ k_col.T) / (2*m)
pos = nx.spring_layout(G, seed=42)
labels = {node: node for node in G.nodes()}
all_metrics = {'degree': defaultdict(dict),'betweenness': defaultdict(dict),'closeness': defaultdict(dict),'clustering': defaultdict(dict)}
visualization_steps = []

# Helpers
def compute_and_store_metrics(G, iteration, all_metrics):
    if iteration in all_metrics['degree']:
        return
    all_metrics['degree'][iteration] = nx.degree_centrality(G)
    all_metrics['betweenness'][iteration] = nx.betweenness_centrality(G)
    all_metrics['closeness'][iteration] = nx.closeness_centrality(G)
    all_metrics['clustering'][iteration] = nx.clustering(G)

def draw_communities_save(G, pos, labels, communities_list, title, fname):
    plt.figure(figsize=(8,6))
    node_colors = np.zeros(G.number_of_nodes())
    cmap = plt.get_cmap('tab20')
    for i, com in enumerate(communities_list):
        for node in com:
            node_colors[node] = i
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, cmap=cmap, node_size=300)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8)
    plt.title(title)
    plt.axis('off')
    plt.savefig(fname)
    plt.close()

# Recursive partition
import numpy.linalg as la

def recursive_spectral_partition(nodes, B, G, pos, labels, all_metrics, current_communities, iteration_counter):
    iteration = iteration_counter[0]
    iteration_counter[0] += 1
    compute_and_store_metrics(G, iteration, all_metrics)
    visualization_steps.append((list(current_communities), f"Iteration {iteration} (Splitting {len(nodes)} nodes)"))
    if len(nodes) <= 1:
        return [nodes]
    B_restricted = B[np.ix_(nodes, nodes)]
    try:
        eigenvalues, eigenvectors = la.eigh(B_restricted)
    except la.LinAlgError:
        return [nodes]
    lambda_1 = eigenvalues[-1]
    u_1 = eigenvectors[:, -1]
    if lambda_1 <= 1e-10:
        return [nodes]
    group_pos, group_neg = [], []
    for i, node_id in enumerate(nodes):
        if u_1[i] >= 0:
            group_pos.append(node_id)
        else:
            group_neg.append(node_id)
    if not group_pos or not group_neg:
        return [nodes]
    next_communities = [c for c in current_communities if c != nodes]
    next_communities.append(group_pos)
    next_communities.append(group_neg)
    communities_pos = recursive_spectral_partition(group_pos, B, G, pos, labels, all_metrics, list(next_communities), iteration_counter)
    final_communities_after_pos = [c for c in next_communities if c not in communities_pos] + communities_pos
    communities_neg = recursive_spectral_partition(group_neg, B, G, pos, labels, all_metrics, final_communities_after_pos, iteration_counter)
    return communities_pos + communities_neg

# Run
if __name__ == '__main__':
    print('Starting recursive partitioning...')
    initial_nodes = list(G.nodes())
    iteration_counter = [0]
    final_communities = recursive_spectral_partition(initial_nodes, B, G, pos, labels, all_metrics, [initial_nodes], iteration_counter)
    final_iter = iteration_counter[0]
    compute_and_store_metrics(G, final_iter, all_metrics)
    print('...Partitioning complete.')
    print(f'Found {len(final_communities)} communities.')
    for i, community in enumerate(final_communities):
        print(f' Community {i+1}: {sorted(community)}')
    # Save visualizations
    for i, (coms, title) in enumerate(visualization_steps):
        draw_communities_save(G, pos, labels, coms, title, f'visual_{i}.png')
    # Plot one metric (betweenness) to file
    import matplotlib.pyplot as plt
    plt.figure()
    metric = 'betweenness'
    metric_data = all_metrics[metric]
    iterations = sorted(metric_data.keys())
    for node in sorted(G.nodes()):
        y = [metric_data[it].get(node,0) for it in iterations]
        plt.plot(iterations, y, alpha=0.3, color='gray')
    plt.plot(iterations, [metric_data[it].get(0,0) for it in iterations], 'o-', color='blue', label='0')
    plt.plot(iterations, [metric_data[it].get(33,0) for it in iterations], 's-', color='red', label='33')
    plt.legend()
    plt.xlabel('Iteration')
    plt.ylabel('Betweenness')
    plt.savefig('betweenness_evolution.png')
    plt.close()
    print('Saved visual_*.png and betweenness_evolution.png')
