from datetime import date
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

G.node[1]['occupation'] = 'scientist'
G.node[2]['occupation'] = 'programmer'
G.node[3]['occupation'] = 'tester'
G.node[4]['occupation'] = 'scientist'
G.node[5]['occupation'] = 'programmer'
G.node[6]['occupation'] = 'tester'
G.node[7]['occupation'] = 'scientist'
G.node[8]['occupation'] = 'programmer'
G.node[9]['occupation'] = 'tester'
G.node[10]['occupation'] = 'scientist'
G.node[11]['occupation'] = 'programmer'

print(G.nodes(data=True))

G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(1, 5)
G.add_edge(1, 6)
G.add_edge(1, 7)
G.add_edge(1, 8)
G.add_edge(1, 9)
G.add_edge(1, 10)
G.add_edge(1, 11)
G.add_edge(2, 8)
G.add_edge(8, 11)



G.edges[1,2]['date'] = date(2010, 1, 1)

G.edges[1,2]['weight'] = 2

print(G.edges(data=True))

nx.draw(G, with_labels=True)

plt.show()

# Use a list comprehension to get the nodes of interest: noi
noi = [n for n, d in G.nodes(data=True) if d.get('occupation') == 'scientist']

# Use a list comprehension to get the edges of interest: eoi
eoi = [(u, v) for u, v, d in G.edges(data=True) if not d.get('date') is None and d.get('date') < date(2010, 1, 1)]

# Iterate over all the edges (with metadata)
for u, v, d in G.edges(data=True):
    # Check if node 293 is involved
    if 2 in [u, v]:
        # Set the weight to 1.1
        G.edges[u,v]['weight'] = 1.1

# Compute the degree of every node: degrees
degrees = [len(list(G.neighbors(n))) for n in G.nodes()]

# Compute the degree centrality of the Twitter network: deg_cent
deg_cent = nx.degree_centrality(G)

# Plot a scatter plot of the centrality distribution and the degree distribution
plt.figure()
plt.scatter(degrees, list(deg_cent.values()))
plt.show()

# Compute the betweenness centrality of T: bet_cen
bet_cent = nx.betweenness_centrality(G)

# Create a scatter plot of betweenness centrality and degree centrality
plt.scatter(list(bet_cent.values()),list(deg_cent.values()))

# Display the plot
plt.show()

# Compute the maximum degree centrality: max_dc
max_dc = max(deg_cent.values())

# Find the user(s) that have collaborated the most: prolific_collaborators
prolific_collaborators = [n for n, dc in deg_cent.items() if dc == max_dc]

# Print the most prolific collaborator(s)
print(prolific_collaborators)



# Import nxviz
import nxviz as nv

# Create the MatrixPlot object: m
m = nv.MatrixPlot(G)

# Draw m to the screen
m.draw()

# Display the plot
plt.show()

# Convert T to a matrix format: A
A = nx.to_numpy_matrix(G)

# Convert A back to the NetworkX form as a directed graph: G_conv
G_conv = nx.from_numpy_matrix(A, create_using=nx.DiGraph())

# Check that the `category` metadata field is lost from each node
for n, d in G_conv.nodes(data=True):
    assert 'category' not in d.keys()


# Create the CircosPlot object: c
c = nv.CircosPlot(G)

# Draw c to the screen
c.draw()

# Display the plot
plt.show()


# Create the un-customized ArcPlot object: a
a = nv.ArcPlot(G,node_order='occupation',node_color='occupation')

a.draw()

plt.show()

# Identify the largest maximal clique: largest_max_clique
largest_max_clique = set(sorted(nx.find_cliques(G), key=lambda x: len(x))[-1])

# Create a subgraph from the largest_max_clique: G_lmc
G_lmc = nx.Graph(G.subgraph(largest_max_clique))

# Go out 1 degree of separation
for node in list(G_lmc.nodes()):
    G_lmc.add_nodes_from(G.neighbors(node))
    G_lmc.add_edges_from(zip([node] * len(list(G.neighbors(node))), G.neighbors(node)))

# Record each node's degree centrality score
for n in G_lmc.nodes():
    G_lmc.node[n]['degree centrality'] = nx.degree_centrality(G_lmc)[n]

# Create the ArcPlot object: a
b = nv.ArcPlot(G_lmc,node_order='degree centrality')

# Draw the ArcPlot to the screen
b.draw()
plt.show()

# Import necessary modules
from itertools import combinations
from collections import defaultdict

# Initialize the defaultdict: recommended
recommended = defaultdict(int)

# Iterate over all the nodes in G
for n, d in G.nodes(data=True):

    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n), 2):

        # Check whether n1 and n2 do not have an edge
        if not G.has_edge(n1, n2):
            # Increment recommended
            recommended[(n1, n2)] += 1

# Identify the top 10 pairs of users
all_counts = sorted(recommended.values())
top10_pairs = [pair for pair, count in recommended.items() if count > all_counts[-10]]
print(top10_pairs)

