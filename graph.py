"""
Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі 
(наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).

INFO
📖 Реальну мережу можна вибрати на свій розсуд, 
якщо немає можливості придумати свою мережу, наближену до реальності.

Візуалізуйте створений граф, проведіть аналіз основних характеристик 
(наприклад, кількість вершин та ребер, ступінь вершин).
"""


import networkx as nx
import matplotlib.pyplot as plt


# Створення графа
G = nx.Graph()

# Додавання вершин (станцій метро)
stations = ["Station A", "Station B", "Station C", "Station D", "Station E", "Station F"]
G.add_nodes_from(stations)

# Додавання ребер (з'єднань між станціями)
edges = [("Station A", "Station B"), 
         ("Station A", "Station C"), 
         ("Station B", "Station D"), 
         ("Station C", "Station D"), 
         ("Station D", "Station E"), 
         ("Station E", "Station F")]

G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)  # позиціонування вузлів

nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue")
nx.draw_networkx_edges(G, pos, width=2, edge_color="grey")
nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")

plt.title("Transport Network")
plt.show()

# Аналіз графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print("Degree centrality of nodes:")
for node, centrality in degree_centrality.items():
    print(f"{node}: {centrality:.2f}")
