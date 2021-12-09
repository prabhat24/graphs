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


def print_all_paths(graph, src, dest, visited, psf):
	if src == dest:
		print(psf)
	else:
		neighbours = graph.graph.get(src, None)
		visited[src] = True
		if neighbours:
			for neighbour in neighbours:
				if visited.get(neighbour.dest, False) == False:
					print_all_paths(graph, neighbour.dest, dest, visited, psf + " " + str(neighbour.dest))
		visited[src] = False

if __name__ == '__main__':
	vertex = 7
	edges = 8
	graph = Graph(vertex)
	adj_list = [
		[0 ,1, 10],
		[1, 2, 10],
		[2, 3, 10],
		[0, 3, 10],
		[3, 4, 10],
		[4, 5, 10],
		[5, 6, 10],
		[4, 6, 10],
	]
	for lst in adj_list:
		graph.add_edge(*lst, is_bidirectional=True)
	display(graph.graph)
	source = 0
	destination = 6
	print_all_paths(graph, source, destination, dict(), str(source))
