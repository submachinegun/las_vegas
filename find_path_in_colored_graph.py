#!/user/bin/python
"""
Given a directed graph G, with nodes colored black, green or red.
Find all vertex s such that from s there is a path which contains at least one green vertex and ends with red vertex
"""


import unittest


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
		rtype: [Vertex.index]
		"""
		tail_red_nodes = filter(lambda x: x.color == 'r', set(G.vertices) - set(G.edges.keys()))
		indegree = [0] * len(G.vertices)
		for nei_list in G.edges.values():
			for v in nei_list:
				indegree[v.index] += 1
		head_nodes = filter(lambda x: indegree[x.index] == 0, G.vertices)
		ret = []
		for node in tail_red_nodes:
			print 'tail '+str(node.index)
		for node in head_nodes:
			print 'head '+str(node.index)
		for node in head_nodes:
			if self.dfs_find_pattern_paths_head(G, node, tail_red_nodes, 0):
				ret.append(node.index)
		return ret

	def dfs_find_pattern_paths_head(self, G, node, tail_red_nodes, green_num):
		if node not in G.edges:  # not in G.edges means leaf node
			if green_num >= 1 and node in tail_red_nodes:
				return True
			return False
		for nei in G.edges[node]:
			if node.color == 'g':
				return self.dfs_find_pattern_paths_head(G, nei, tail_red_nodes, green_num + 1)
			else:
				return self.dfs_find_pattern_paths_head(G, nei, tail_red_nodes, green_num)


class MyclassTest(unittest.TestCase):
	def test_example(self):
		v0, v1, v2, v3, v4, v5 = Vertex(0, 'b'), Vertex(1, 'r'), Vertex(2, 'g'), Vertex(3, 'g'), Vertex(4, 'r'), Vertex(5, 'b')
		vertices = [v0, v1, v2, v3, v4, v5]
		edges = {v0:[v2], v1:[v2], v2:[v3], v3:[v4, v5]}
		G = Graph(vertices, edges)
		mm = Myclass()
		self.assertTrue( mm.find_pattern_paths_head(G), ['0', '1'])
		v0, v1, v2, v3 = Vertex(0, 'r'), Vertex(1, 'g'), Vertex(2, 'g'), Vertex(3, 'r')
		v5, v6, v7 = Vertex(5, 'g'), Vertex(6, 'g'), Vertex(7, 'r')
		vertices2 = [v0, v1, v2, v3, v4, v5, v6, v7]
		edges2 = {v0:[v1], v1:[v2], v2:[v3], v3:[v0], v5:[v6], v6:[v7]}
		G2 = Graph(vertices2, edges2)
		self.assertTrue(mm.find_pattern_paths_head(G2), ['0', '5'])
			
if __name__ == '__main__':
	unittest.main()
	
