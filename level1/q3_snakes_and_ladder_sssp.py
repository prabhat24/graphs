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
		for ver in graph.graph.get(cur_vertex, []):
			if distance.get(ver, None) is None:
				d.append(ver)
				distance[ver] = distance[cur_vertex] + 1
		d.popleft()
	return distance


if __name__ == '__main__':
	board = [0] * 37

	# ladders 
	board[2] = 13
	board[9] = 18
	board[18] = 11
	board[25] = 10
	board[5] = 2

	# snakes
	board[17] = -13
	board[24] = -8 
	board[34] = -22
	board[32] = -2

	graph = Graph(37)
	for i in range(0, 37):
		for dice_roll in range(1, 7):
			end_pt =  i + dice_roll
			if end_pt > 36:
				continue
			end_pt += board[end_pt]
			graph.add_edge(i, end_pt, False)
	print(graph.graph)
	print(bfs_sssp(graph, 0))

