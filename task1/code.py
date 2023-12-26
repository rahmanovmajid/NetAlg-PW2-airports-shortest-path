import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
# import tkinter
matplotlib.use('TkAgg')

#1:
data = pd.read_csv('cities_in_az.csv')
G = nx.from_pandas_edgelist(data, source='Origin', target='Destiny', edge_attr=True ,create_using=nx.DiGraph())
nx.draw_networkx(G, with_labels=True)
plt.show()

#2:
print('Path between Baku and Imishli is: => {} without weights'.format(nx.shortest_path(G, source="Baku", target="Imishli")))
print('Path between Baku and Imishli is: => {} with weights'.format(nx.shortest_path(G, source="Baku", target="Imishli",weight='Hours')))
#Reason : weights

nx.add_path(G, ['Baku', 'Imishli'])
G.edges['Baku', 'Imishli']['Hours'] = 1.29

print('Path between Baku and Imishli is: => {} '.format(nx.shortest_path(G, source="Baku", target="Imishli",weight='Hours')))
print('Path between Imishli and Baku is: => {}'.format(nx.shortest_path(G, source="Imishli", target="Baku",weight='Hours')))
#Reason: It's digraph, and the direction is not dual, it's monodirectional for Baku to Imishli
