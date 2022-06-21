import threading 
import heapq


class Edge:
    def __init__(self,src,nbr,wt):
        self.src = src
        self.nbr = nbr
        self.wt=wt

def min_spanning(src, graph, visited):
    h = []
    heapq.heappush(h, [0, -1, src])
    while len(h):
        dis, av, ele = heapq.heappop(h)
        if visited.get(ele, False) == False:
            visited[ele] = True
            if av != -1:
                print("[{}-{}@{}]".format(str(ele), str(av), str(dis)))
            for neigh in graph.get(ele, []):
                if visited.get(neigh.nbr, False) == False:
                    heapq.heappush(h, [neigh.wt, ele, neigh.nbr])
        else:
            continue

def main():
    vtces = int(input())
    edges = int(input()) 
    graph = {}
    for i in range(vtces):
        graph[i] = []
    
    for i in range(edges): 
        lines = input().split(" ")
        v1=int(lines[0])
        v2=int(lines[1])
        wt=int(lines[2])
        e1 = Edge(v1 ,v2 ,wt)
        e2 = Edge(v2 ,v1 ,wt)
        graph[e1.src].append(e1)
        graph[e2.src].append(e2)
    
        #Write your code here
    src = list(graph.keys())[0]
    visited = {}
    min_spanning(src, graph, visited)

if __name__ == '__main__':
    main()
