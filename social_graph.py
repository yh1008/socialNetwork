import networkx as nx
import matplotlib.pyplot as plt
import re
from collections import defaultdict

def draw_graph(graph, labels=None, graph_layout='spring',
               node_size=1600, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

	# create networkx graph
	G=nx.Graph()
	# add edges
	for edge in graph:
		G.add_edge(edge[0], edge[1])

	# these are different layouts for the network you may try
	if graph_layout == 'spring':
		graph_pos=nx.spring_layout(G)
	elif graph_layout == 'spectral':
		graph_pos=nx.spectral_layout(G)
	elif graph_layout == 'random':
		graph_pos=nx.random_layout(G)
	else:
		graph_pos=nx.shell_layout(G)

	# draw graph
	nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, alpha=node_alpha, node_color=node_color)
	nx.draw_networkx_edges(G,graph_pos,width=edge_tickness, alpha=edge_alpha,edge_color=edge_color)
	nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,font_family=text_font)

	plt.show()

def getFriendship():
	friends = []
	friendship = defaultdict(list)
	with open("friends.txt") as input_file:
		for line in input_file:
			empty = re.match(r'^\s*$', line)			
			if empty:
				continue
			else:
				sentence = line	
				sentence = sentence.replace("\n", "")		
				match = re.search(r'Person:', sentence)
				if match:
					sentence = sentence.replace("Person: ", "")
					person = sentence 
				else: 
					sentence = sentence.replace("Friends: ", "")
					sentence = sentence.replace(",","")
					friends = sentence.split(" ")
					#{'Emily': [['Viven', 'Ivy', 'Joel', 'Dennis', 'Json']]})
					friendship[person].append(friends)
		return friendship

def getGraph(dic):
	graph = []
	for person in dic:
		for friend_list in dic[person]:
			for friend in friend_list:
				friendship_tuple = person,friend 
				graph.append (friendship_tuple)
	return graph
	
friendship_dic = getFriendship()
graph = getGraph(friendship_dic)
draw_graph(graph)

