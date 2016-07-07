#!/user/bin/python
"""
Given a directed graph G, with nodes colored black, green or red.
Find all vertex s such that from s there is a path which contains at least one green vertex and ends with red vertex
"""


class Vertex:
	def __init__(self, i, c):
		self.color = c
		self.index = i


class Graph:
	def __init__(self, v, e):
		"""
		:type vertices: [Vertex]
		:type edges: {Vertex: [Vertex]}
		"""
		self.vertices = v
		self.edges = e


class Myclass:
	def find_pattern_paths_head(self, G):
		"""
		:type G: Graph
		rtype: [Vertex]
		"""
		tail_red_nodes = filter(lambda x: x.color == 'r', G.vertices - G.edges.keys())
		indegree = [0] * len(G.vertices)
		for nei_list in G.edges.values():
			for v in nei_list:
				indegree[v.index] += 1
		head_nodes = filter(lambda x: indegree[x.index] == 0, G.vertices)
		ret = []
		for node in head_nodes:
			if self.dfs_find_pattern_paths_head(G, node, tail_red_nodes, 0):
				ret.append(node)
		return ret

	def dfs_find_pattern_paths_head(self, G, node, tail_red_nodes, green_num):
		if node not in G.edges:
			if green_num >= 1 and node in tail_red_nodes:
				return True
			return False
			for nei in G.edges[node]:
				if node.color == 'g':
					return self.dfs_find_pattern_paths_head(G, nei, tail_red_nodes, green_num + 1)
				else:
					return self.dfs_find_pattern_paths_head(G, nei, tail_red_nodes, green_num)
		
if __name__ == '__main__':
	v0, v1, v2, v3, v4, v5 = Vertex(0, 'b'), Vertex(1, 'r'), Vertex(2, 'g'), Vertex(3, 'g'), Vertex(4, 'r'), Vertex(5, 'b')
	vertices = [v0, v1, v2, v3, v4, v5]
	edges = {v0:[v2], v1:[v2], v2:[v3], v3:[v4, v5]}
	G = Graph(vertices, edges)
	mm = Myclass()
	mm.find_pattern_paths_head(G) 
