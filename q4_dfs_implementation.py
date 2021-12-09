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


def dfs(graph, st_vertex, visited):
	print(st_vertex)
	visited[st_vertex] = True
	for ver in graph.graph.get(st_vertex, []):
		if not visited.get(ver, False):
			dfs(graph, ver, visited)


if __name__ == '__main__':
	graph = Graph(7)
	graph.add_edge(1, 2, True)
	graph.add_edge(1, 3, True)
	graph.add_edge(2, 4, True)
	graph.add_edge(4, 7, True)
	graph.add_edge(5, 7, True)
	graph.add_edge(5, 6, True)
	graph.add_edge(5, 3, True)
	print(graph.graph)
	dfs(graph, 1, dict())