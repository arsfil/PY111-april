from typing import Any
import networkx as nx
import matplotlib as plt
import numpy as np

g = {
	('A', 'B'),
	('A', 'C'),
	('A', 'D'),
	('B', 'E'),
	('D', 'F'),
	('E', 'G'),
	('F', 'G'),
	('G', 'H')
}

start_node = 'A'

g.nodes = [
	# [A, B, C, D, E, F, G, H]
	[0, 1, 1, 1, 0, 0, 0, 0],
	[1, 0, 0, 0, 1, 0, 0, 0],
	[1, 0, 0, 0, 0, 0, 0, 0],
	[1, 0, 0, 0, 0, 1, 0, 0],
	[0, 1, 0, 0, 0, 0, 1, 0],
	[0, 0, 0, 1, 0, 0, 1, 0],
	[0, 0, 0, 0, 1, 1, 0, 1],
	[0, 0, 0, 0, 0, 0, 1, 0]
]


nx.draw(g, with_label=True)
plt.show()

def bfs(g: nx.Graph, start_node: Any) -> list:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""

	print(g, start_node)
	return list(g.nodes)
