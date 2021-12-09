from collections import deque

class Graph():
	def __init__(self, vertices):
		self.total_vertices = vertices
		self.graph = dict()

	def add_edge(self, source, dest, is_bydirectional):
		source_list = self.graph.get(source, [])
		source_list.append(dest)
		self.graph[source] = source_list

		if is_bydirectional:
			dest_list = self.graph.get(dest, [])
			dest_list.append(source)
			self.graph[dest] = dest_list


def bfs_sssp(graph, st_vertex):
	distance = dict()
	d = deque()
	d.append(st_vertex)
	distance[st_vertex] = 0
	while len(d) != 0:
		cur_vertex = d[0]
		for ver in graph.graph[cur_vertex]:
			if distance.get(ver, None) is None:
				d.append(ver)
				distance[ver] = distance[cur_vertex] + 1
		d.popleft()
		print(distance)
	return distance


if __name__ == '__main__':
	graph = Graph(6)
	graph.add_edge(1, 2, True)
	graph.add_edge(2, 3, True)
	graph.add_edge(1, 3, True)
	graph.add_edge(3, 5, True)
	graph.add_edge(5, 6, True)
	graph.add_edge(6, 7, True)
	graph.add_edge(7, 5, True)
	graph.add_edge(2, 4, True)
	print(graph.graph)
	print(bfs_sssp(graph, 4))