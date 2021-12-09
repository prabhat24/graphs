import sys

class Graph():
	class Node:
		def __init__(self, src, dest, wt):
			self.src = src
			self.dest = dest
			self.wt = wt

	def __init__(self, vertex):
		self.V = vertex
		self.graph = dict()

	def add_edge(self, src, dest, wt, is_bidirectional): 
		src_list = self.graph.get(src, [])
		src_list.append(self.Node(src, dest, wt))
		self.graph[src] = src_list
		if is_bidirectional:
			dest_list = self.graph.get(dest, [])
			dest_list.append(self.Node(dest, src, wt))
			self.graph[dest] = dest_list

def display(adj_list):
	for k, values in adj_list.items():
		print("____________", "vertex", k, "______________")
		for j in values:
			print("src: ", j.src, "dest :", j.dest, "wt: ", j.wt)

class Solution:
	nodelist = list()
	total_list = list()

	@classmethod
	def get_connected_components(cls, graph, visited):
		for key in graph.graph.keys():
			if visited.get(key, False) == False:
				cls.dfs(graph, key, visited)
				cls.total_list.append(cls.nodelist)
				cls.nodelist = list()

	@classmethod
	def dfs(cls, graph, src, visited):
		cls.nodelist.append(src)
		visited[src] = True
		neighbours = graph.graph.get(src, None)
		if neighbours:
			for neighbour in neighbours:
				if visited.get(neighbour.dest, False) == False:
					Solution.dfs(graph, neighbour.dest, visited)

if __name__ == '__main__':
	vertex = 7
	edges = 8
	graph = Graph(vertex)
	adj_list = [
		[0 ,1, 10],
		[2, 3, 10],
		[4, 5, 10],
		[5, 6, 10],
		[4, 6, 10],
	]
	for lst in adj_list:
		graph.add_edge(*lst, is_bidirectional=True)
	display(graph.graph)
	Solution.get_connected_components(graph, dict())
	print(Solution.total_list)

