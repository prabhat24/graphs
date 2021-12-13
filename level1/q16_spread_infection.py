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


def bfs(graph, st_vertex, time):
	visited = dict()
	d = deque()
	d.append((st_vertex, 0))
	count = 0
	while len(d) != 0:
		cur_vertex, level = d[0]
		if level > time:
			break 
		d.popleft()
		if visited.get(cur_vertex, -1) == -1:
			visited[cur_vertex] = level
			count = count + 1
			for ver in graph.graph.get(cur_vertex, []):
				if not visited.get(ver, False):
					d.append((ver, level + 1))
	return count

if __name__ == '__main__':
	graph = Graph(7)
	graph.add_edge(0, 1, True)
	graph.add_edge(1, 2, True)
	graph.add_edge(2, 3, True)
	graph.add_edge(0, 3, True)
	graph.add_edge(3, 4, True)
	graph.add_edge(2, 5, True)
	graph.add_edge(4, 5, True)
	graph.add_edge(4, 6, True)
	graph.add_edge(5, 6, True)
	print(graph.graph)
	print(bfs(graph, 6, 3))