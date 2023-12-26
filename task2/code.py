import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
# import tkinter
matplotlib.use('TkAgg')

data = pd.read_csv("airports.csv")
G = nx.from_pandas_edgelist(data, source="Origin", target="Dest", edge_attr=True, create_using=nx.DiGraph)
nx.draw_networkx(G, with_labels=True)
plt.show()

print('Shortest distance between "CRP" and "BOI" is: {}'.format(nx.shortest_path(G, source="CRP", target="BOI",weight='Distance')))
print('Shortest distance between "BOI" and "CRP" is: {}'.format(nx.shortest_path(G, source="BOI", target="CRP",weight='Distance')))

print('Smallest flight time  between "CRP" and "BOI" is: {}'.format(nx.shortest_path(G, source="CRP", target="BOI",weight='AirTime')))
print('Smallest flight time between "BOI" and "CRP" is: {}'.format(nx.shortest_path(G, source="BOI", target="CRP",weight='AirTime')))
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('Closeness Centrality of CRP due to distance: {}'.format(nx.closeness_centrality(G, u = "CRP", distance = "Distance")))
print('Closeness Centrality of BOI due to distance: {}'.format(nx.closeness_centrality(G, u = "BOI", distance = "Distance")))

print('Closeness Centrality of CRP due to flight time: {}'.format(nx.closeness_centrality(G, u = "CRP", distance = "Airtime")))
print('Closeness Centrality of BOI due to flisght time: {}'.format(nx.closeness_centrality(G, u = "BOI", distance = "Airtime")))

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('Betweeness Centrality for Distance: ')
print(nx.betweenness_centrality(G,weight= "Distance"))
print('Betweeness Centrality for Flight time: ')
print(nx.betweenness_centrality(G,weight= "AirTime"))
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('Network Density is: {}'.format(nx.density(G)))
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('Network Diameter is: {}'.format(nx.diameter(G)))
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('Network Average Path Length: {}'.format(nx.average_shortest_path_length(G)))
