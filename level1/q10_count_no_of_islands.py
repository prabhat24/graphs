
def no_of_islands(arr, R, C, visited):
	count = 0 
	for i in range(0, R):
		for j in range(0, C):
			if visited[i][j] == False and arr[i][j] != 1:
				dfs(arr, i, j, R, C, visited)
				count += 1
	return count

def dfs(arr, srci, srcj, R, C, visited):
	if srci >= R or srcj >= C or arr[srci][srcj] == 1 or visited[srci][srcj]:
		return
	visited[srci][srcj] = True
	dfs(arr, srci -1, srcj, R, C, visited)
	dfs(arr, srci, srcj-1, R, C, visited)
	dfs(arr, srci + 1, srcj, R, C, visited)
	dfs(arr, srci, srcj + 1, R, C, visited)



if __name__ == '__main__':
	R = 8
	C = 8
	arr = [
		[0, 0, 1, 1, 1, 1, 1, 1],
		[0, 0, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 0],
		[1, 1, 0, 0, 0, 1, 1, 0],
		[1, 1, 1, 1, 0, 1, 1, 0],
		[1, 1, 1, 1, 0, 1, 1, 0],
		[1, 1, 1, 1, 1, 1, 1, 0],
		[1, 1, 1, 1, 1, 1, 1, 0],
	]
	visited = [ [False] * C for k in range(0, R) ]
	print(no_of_islands(arr, R, C, visited))