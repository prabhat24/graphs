import sys
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

class Solution:
	l_cost_path = ""
	m_cost_path = ""
	l_cost = 1<<32 - 1
	m_cost = 0
	floor_path = ""
	floor_path_cost = 0
	ceil_path = ""
	ceil_path_cost = 1<<32 - 1
	h = list()
	@classmethod
	def stats_for_all_paths(cls, graph, src, dest, visited, wsf, psf, criteria):
		if src == dest:
			if wsf < cls.l_cost:
				cls.l_cost = wsf
				cls.l_cost_path = psf
			if wsf > cls.m_cost:
				cls.m_cost = wsf
				cls.m_cost_path = psf
			if wsf <= criteria and wsf >= cls.floor_path_cost:
				cls.floor_path_cost = wsf
				cls.floor_path = psf
			if wsf > criteria  and wsf <= cls.ceil_path_cost:
				cls.ceil_path_cost = wsf
				cls.ceil_path = psf
			# kth smallest/ largest
			heapq.heappush(cls.h, (wsf, psf))

		else:
			neighbours = graph.graph.get(src, None)
			visited[src] = True
			if neighbours:
				for neighbour in neighbours:
					if visited.get(neighbour.dest, False) == False:
						print("src:", src, "neighbour", neighbour.dest)
						Solution.stats_for_all_paths(graph, neighbour.dest, dest, visited, wsf + neighbour.wt ,psf + " " + str(neighbour.dest), criteria)
			visited[src] = False

if __name__ == '__main__':
	vertex = 7
	edges = 8
	graph = Graph(vertex)
	adj_list = [
		[0 ,1, 10],
		[1, 2, 10],
		[2, 3, 10],
		[0, 3, 40],
		[3, 4, 2],
		[4, 5, 3],
		[5, 6, 3],
		[4, 6, 8],
	]
	for lst in adj_list:
		graph.add_edge(*lst, is_bidirectional=True)
	display(graph.graph)
	source = 0
	destination = 6
	k = 2
	Solution.stats_for_all_paths(graph, source, destination, dict(), 0, str(source), 40)
	print('lcost_path', Solution.l_cost_path)
	print('l_cost', Solution.l_cost)
	print('m_cost_path', Solution.m_cost_path)
	print('mcost', Solution.m_cost)
	print('floor_path', Solution.floor_path)
	print('floor_path_cost', Solution.floor_path_cost)
	print('ceil_path', Solution.ceil_path)
	print('ceil_path_cost', Solution.ceil_path_cost)
	print('kth largest', Solution.h[len(Solution.h)-k])
	print('kth smallest', Solution.h[k - 1])

