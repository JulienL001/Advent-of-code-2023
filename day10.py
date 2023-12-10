from collections import defaultdict
from itertools import product, combinations, permutations
import numpy as np
import math

file = open('day10.txt', 'r', encoding='utf-8-sig')
# lines = file.read().splitlines()
# lines =''''''.splitlines()
grid = np.array([list(line) for line in file.read().splitlines()])
# grid =''''''.splitlines()
# directions = {'>': (1,0), '^':(0,1), '<':(-1,0), 'v':(0,-1)}
directions = [(1,0), (0,1), (-1,0), (0,-1)]
# directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)] # all directions around
# L = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# visited = set()
# d = defaultdict(int)
# m, n = len(grid), len(grid[0])

########################################
# part 1

# finds start position
m, n = grid.shape
for i, j in product(range(n), range(m)):
    if grid[i, j] == 'S':
        start = (i, j)
        break
    
i0, j0 = start

# finds start direction
for ((di0, dj0), connected_pipe) in zip(directions, ['|LJ', '-7J', '|F7', '-FL']):
    if grid[i0 + di0, j0+ dj0] in connected_pipe: break

# brows the loop
loop = {start}
pipes_number = 1
di, dj = di0, dj0
i, j = i0 + di, j0 + dj
while (i, j) != start:
    loop.add((i,j))
    if (di, dj) == (0, 1):
        if grid[i, j] == 'J' : di, dj = -1, 0
        if grid[i, j] == '7' : di, dj = 1, 0
    elif (di, dj) == (0, -1):
        if grid[i, j] == 'F' : di, dj = 1, 0
        if grid[i, j] == 'L' : di, dj = -1, 0
    elif (di, dj) == (1, 0):
        if grid[i, j] == 'L' : di, dj = 0, 1
        if grid[i, j] == 'J' : di, dj = 0, -1
    elif (di, dj) == (-1, 0):
        if grid[i, j] == 'F' : di, dj = 0, 1
        if grid[i, j] == '7' : di, dj = 0, -1
    i, j = i + di, j + dj
    
print(len(loop)//2)

########################################   
# part 2

# extends the grid and marks the loop with stars
big_grid = np.full((2*m+1, 2*n+1), '.', dtype = str)
for i, j in product(range(n), range(m)):
    if (i, j) not in loop:
        continue
    I, J = 2*i+1, 2*j+1
    big_grid[I, J] = '*'
    if grid[i, j] in '-FL' : big_grid[I, J+1] = '*'
    if grid[i, j] in '|F7' : big_grid[I+1, J] = '*'

# searchs for tiles and junk pipes outside the loop
to_visit = [(0,0)]
visited = set()
while to_visit:
    node = to_visit.pop()
    if node in visited: 
        continue
    visited.add(node)
    i, j = node
    for di, dj in directions:
        I, J = i+di, j+dj
        if 0<=I<2*m+1 and 0<=J<2*n+1 and big_grid[I, J] == '.': 
            to_visit.append((I, J))
            
# count tiles and junk pipes outide the loop in the original grid
outside = len([node for node in visited if (node[0] % 2, node[1] % 2) == (1,1)])

# compute tiles in the loop 
print(m*n - len(loop) - outside)





# old part 2
di, dj = 0,-1
i, j = i0 + di, j0 + dj
to_visit = []
while (i, j) != start:
    Di, Dj = directions[(directions.index((di, dj)) + 1) % 4]
    I, J = i + Di, j + Dj
    if 0 <= I < m and 0<= J < n and (grid[I][J] == '.' or (I, J) not in loop): 
        to_visit.append((I, J))
    
    turned = False
    if (di, dj) == (0, 1):
        if grid[i][j] == 'J' : di, dj = -1, 0
        if grid[i][j] == '7' : di, dj = 1, 0
        turned = True

    elif (di, dj) == (0, -1):
        if grid[i][j] == 'F' : di, dj = 1, 0
        if grid[i][j] == 'L' : di, dj = -1, 0
        turned = True

    elif (di, dj) == (1, 0):
        if grid[i][j] == 'L' : di, dj = 0, 1
        if grid[i][j] == 'J' : di, dj = 0, -1
        turned = True
            
    elif (di, dj) == (-1, 0):
        if grid[i][j] == 'F' : di, dj = 0, 1
        if grid[i][j] == '7' : di, dj = 0, -1
        turned = True
                
    if turned:
        Di, Dj = directions[(directions.index((di, dj)) + 1) % 4]
        I, J = i + Di, j + Dj
        if 0 <= I < m and 0<= J < n and (grid[I][J] == '.' or (I, J) not in loop): 
            to_visit.append((I, J))
            
    i, j = i + di, j + dj
    


visited = set()
while to_visit:
    point = to_visit.pop()
    if point not in visited:
        visited.add(point)        
        i0, j0 = point
        for di, dj in directions:
            i, j = i0 + di, j0 + dj
            if 0 <= i < m and 0 <= j < n and (i, j) not in visited and (grid[i][j] == '.' or (i, j) not in loop):
                to_visit.append((i, j))
print(len(visited))
