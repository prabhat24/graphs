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


def is_bipartite(graph, st_vertex):
	visited = dict()
	d = deque()
	d.append((st_vertex, 0))
	set1, set2 = list(), list() 
	while len(d) != 0:
		cur_vertex, level = d[0]
		d.popleft()
		if visited.get(cur_vertex, -1) == -1:
			visited[cur_vertex] = level
			for ver in graph.graph.get(cur_vertex, []):
				if visited.get(ver, -1) == -1:
					d.append((ver, level + 1))
		else:
			prev_l = visited.get(cur_vertex)
			if prev_l % 2 != level%2:
				return False
	return True


if __name__ == '__main__':
	graph = Graph(7)
	graph.add_edge(0, 1, True)
	graph.add_edge(1, 2, True)
	graph.add_edge(2, 3, True)
	graph.add_edge(0, 3, True)
	print(graph.graph)
	print(is_bipartite(graph, 0))