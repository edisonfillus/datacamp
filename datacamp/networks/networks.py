from datetime import date
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_nodes_from([1, 2, 3])

G.node[1]['occupation'] = 'scientist'
G.node[2]['occupation'] = 'programmer'
G.node[3]['occupation'] = 'tester'

print(G.nodes(data=True))

G.add_edge(1, 2)

G.edges[1,2]['date'] = date(2010, 1, 1)

G.edges[1,2]['weight'] = 2

print(G.edges(data=True))

#nx.draw(G)

#plt.show()

# Use a list comprehension to get the nodes of interest: noi
noi = [n for n, d in G.nodes(data=True) if d.get('occupation') == 'scientist']

# Use a list comprehension to get the edges of interest: eoi
eoi = [(u, v) for u, v, d in G.edges(data=True) if d.get('date') < date(2010, 1, 1)]

# Iterate over all the edges (with metadata)
for u, v, d in G.edges(data=True):
    # Check if node 293 is involved
    if 2 in [u, v]:
        # Set the weight to 1.1
        G.edges[u,v]['weight'] = 1.1


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