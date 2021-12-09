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



def dfs(graph, src, visited, single_component):
	visited[src] = True
	single_component.append(src)

	neighbours = graph.graph.get(src, None)

	for neighbour in neighbours:
		if visited.get(neighbour, False) == False:
			dfs(graph, neighbour, visited, single_component)


def get_graph_components(graph, visited):
	# iterate over all the vertex and find out total graphs conponets
	# return the list of lists where each list contains the vetices in each component
	all_components = []
	for v in range(graph.total_vertices):
		if visited.get(v, False) == False:
			single_component = []
			dfs(graph, v, visited, single_component)
			all_components.append(single_component)
	return all_components



def no_of_perfect_friends(graph):
	friends = 0
	components = get_graph_components(graph, dict())
	for i in range(0, len(components)):
		for j in range(i +1, len(components)):
			friends += len(components[i]) * len(components[j])
	return friends


if __name__ == '__main__':
	vertex = 7
	graph = Graph(7)
	graph.add_edge(0, 1, True)
	graph.add_edge(2, 3, True)
	graph.add_edge(4, 5, True)
	graph.add_edge(5, 6, True)
	graph.add_edge(4, 6, True)
	print(graph.graph)
	print(no_of_perfect_friends(graph))