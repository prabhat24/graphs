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


if __name__ == '__main__':
	graph = Graph(6)
	graph.add_edge("modi", "trump", True)
	graph.add_edge("putin", "trump", False)
	graph.add_edge("putin", "pope", False)
	graph.add_edge("putin", "modi", False)
	graph.add_edge("modi", "yogi", True)
	graph.add_edge("prabhu", "modi", False)
	graph.add_edge("yogi", "prabhu", False)
	print(graph.graph)