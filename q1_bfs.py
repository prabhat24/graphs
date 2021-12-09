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


def bfs(graph, st_vertex):
	visited = dict()
	d = deque()
	d.append(st_vertex)
	visited[st_vertex] = True
	while len(d) != 0:
		cur_vertex = d[0]
		for ver in graph.graph[cur_vertex]:
			if not visited.get(ver, None):
				d.append(ver)
				visited[ver] = True
		print(cur_vertex, end=" ")
		d.popleft()


if __name__ == '__main__':
	graph = Graph(6)
	graph.add_edge("modi", "trump", True)
	graph.add_edge("putin", "trump", True)
	graph.add_edge("putin", "pope", True)
	graph.add_edge("putin", "modi", True)
	graph.add_edge("modi", "yogi", True)
	graph.add_edge("prabhu", "modi", True)
	graph.add_edge("yogi", "prabhu", True)
	print(graph.graph)
	bfs(graph, "modi")