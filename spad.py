import matplotlib.pyplot as plt
import networkx as nx

plt.subplots(2,3,figsize=(15,6))
#二维网格图
G=nx.grid_2d_graph(2,3)
plt.subplot(2,3,1)
nx.draw(G,with_labels=True)
plt.title('grid_2d_graph')
plt.axis('on')
plt.xticks([])
plt.yticks([])

#n维网格图
grid_graph = nx.grid_graph(dim=[2, 4, 4])
plt.subplot(2,3,2)
nx.draw(grid_graph,with_labels=True)
plt.title('grid_graph')
plt.axis('on')
plt.xticks([])
plt.yticks([])

#m×n的六角形格子图。
G=nx.hexagonal_lattice_graph(3,3)
plt.subplot(2,3,3)
nx.draw(G,with_labels=True)
plt.title('hexagonal_lattice_graph')
plt.axis('on')
plt.xticks([])
plt.yticks([])

#n维超立方体图形。
G=nx.hypercube_graph(3)
plt.subplot(2,3,4)
nx.draw(G,with_labels=True)
plt.title('hypercube_graph')
plt.axis('on')
plt.xticks([])
plt.yticks([])

#三角格子图
G=nx.triangular_lattice_graph(11,3)
plt.subplot(2,3,5)
nx.draw(G,with_labels=True)
plt.title('hypercube_graph')
plt.axis('on')
plt.xticks([])
plt.yticks([])

plt.show()