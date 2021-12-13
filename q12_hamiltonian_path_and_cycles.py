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


def all_nodes_visited(visited, graph):
	for node in range(0, graph.V):
		if visited.get(node, False) == False:
			return False
	return True

def print_hamiltonian_paths_cycles(graph, c,src, t_src, visited, psf):
	visited[t_src] = True
	if all_nodes_visited(visited, graph):
		if t_src in [neigh.dest for neigh in graph.graph.get(src, None)]:
			print(psf + " *")
		else:
			print(psf + " .")

		
	else:
		neighbours = graph.graph.get(t_src, None)
		if neighbours:
			for neighbour in neighbours:
				if visited.get(neighbour.dest, False) == False:
					print_hamiltonian_paths_cycles(graph, c+1, src, neighbour.dest, visited, psf + " " + str(neighbour.dest))
	visited[t_src] = False

if __name__ == '__main__':
	vertex = 7
	edges = 9
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
		[2, 5, 10]
	]
	for lst in adj_list:
		graph.add_edge(*lst, is_bidirectional=True)
	display(graph.graph)
	source = 0
	print_hamiltonian_paths_cycles(graph, 0,source, source, dict(), str(source))
