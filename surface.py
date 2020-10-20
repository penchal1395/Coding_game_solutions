"""
Find the surfaces that are connected
"""
def searchlake(root_node, visited, fringe):
  """Return the connected lake
  Args:
    root_node(tuple): value of the coordinates
    visited(list): list of all visted nodes
    fringe(list): all nodes waiting to be expand
  Return:
    lake(list): Coordinates of the connected lake
  """
  while fringe:
    root_node = fringe[0]
    fringe = fringe[1:]
    visited.append(root_node)
    rx, ry = root_node
    if grid[rx][ry] == -1:
        return []
    grid[rx][ry] = 1
    neighbors = [
      (rx - 1, ry), #left
      (rx + 1, ry), #right
      (rx, ry - 1), #top
      (rx, ry + 1), #bottom
    ]
    for neighbor in neighbors:
      nx,ny = neighbor
      if 0 <= nx <= height-1 and 0 <= ny <= width-1 and grid[nx][ny] == 0:
        fringe.append(neighbor)
        grid[nx][ny] = 1
  return visited
width = int(input())
height = int(input())
grid = [[-1 if j=='#' else 0 for j in input()] for i in range(height)]
no_of_coordinates = int(input())
coordinates = [tuple(map(int,input().split()))[::-1] for _ in range(no_of_coordinates)]
visited_lake = {}
for coordinate in coordinates:
  if coordinate in visited_lake:
    print(visited_lake[coordinate])
  else:
    lake = searchlake(coordinate,[],[coordinate])
    for cell in lake:
      visited_lake[cell] = len(lake)
    print(len(lake))