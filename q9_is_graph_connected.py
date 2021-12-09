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
	def is_grapth_connected(cls, graph, visited):
		src = list(graph.graph.keys())[0]
		cls.dfs(graph, src, visited)
		# check if all the nodes are visited
		for key in graph.graph.keys():
			if visited.get(key, False) == False:
				return False
		return True

	@classmethod
	def dfs(cls, graph, src, visited):
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
		[1, 2, 10],
		[2, 3, 10],
		[0, 3, 40],
		[3, 4, 2],
		[4, 5, 3],
		[5, 6, 3],
		[4, 6, 8],
	]
	for lst in adj_list:
		graph.add_edge(*lst, is_bidirectional=True)
	display(graph.graph)
	print(Solution.is_grapth_connected(graph, dict()))
	

