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


def dijkstra_algorithm(graph, st_vertex, psf):
	visited = dict()
	q = list()
	heapq.heappush(q, (0, st_vertex))
	count = 0
	while len(q) != 0:
		wsf, cur_vertex = q[0]

		heapq.heappop(q)
		if visited.get(cur_vertex, False) == False:
			visited[cur_vertex] = True
			psf = psf + str(cur_vertex)
			print(cur_vertex, "@", psf, "|", wsf)
			for ver in graph.graph.get(cur_vertex, []):
				if not visited.get(ver.dest, False):
					heapq.heappush(q, (wsf + ver.wt, ver.dest))
	return count

if __name__ == '__main__':
	vertex = 7
	graph = Graph(vertex)
	adj_list = [
		[0 ,1, 10],
		[1, 2, 10],
		[2, 3, 10],
		[0, 3, 40],
		[3, 4, 2],
		[4, 5, 10],
		[5, 6, 13],
		[4, 6, 11],
	]
	for lst in adj_list:
		graph.add_edge(*lst, is_bidirectional=True)
	display(graph.graph)
	dijkstra_algorithm(graph, 0, "")