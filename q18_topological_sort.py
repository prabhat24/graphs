from collections import deque
import heapq 

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



def topological_sort(graph, st_vertex, st, visited):
	visited[st_vertex] = True
	neighbours = graph.graph.get(st_vertex, [])
	for neighbour in neighbours:
		if visited.get(neighbour.dest, False) == False:
			topological_sort(graph, neighbour.dest, st, visited)
	st.appendleft(st_vertex)
	
if __name__ == '__main__':
	vertex = 7
	graph = Graph(vertex)
	adj_list = [
		[0 ,1, 10, False],
		[1, 2, 10, False],
		[2, 3, 10, False],
		[0, 3, 40, False],
		[4, 3, 2, False],
		[4, 5, 10, False],
		[5, 6, 13, False],
		[4, 6, 11, False],
	]
	st = deque()
	for lst in adj_list:
		graph.add_edge(*lst)
	visited = dict()
	display(graph.graph)
	for key in graph.graph.keys():
		if visited.get(key, False) == False:
			topological_sort(graph, key, st, visited)	
	print(st)
