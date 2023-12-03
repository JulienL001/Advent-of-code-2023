from collections import defaultdict
import numpy as np

file = open('day03.txt', 'r', encoding='utf-8-sig')
grid = file.read().splitlines()
# lines ='''
# '''.splitlines()
# directions = {'>': (1,0), '^':(0,1), '<':(-1,0), 'v':(0,-1)}
# directions = [(1,0), (0,1), (-1,0), (0,-1)]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)] # all directions around
# L = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# visited = set()
# d = collections.defaultdict(int)

# part 1
somme = 0
m = len(grid)
for i,line in enumerate(grid):
    n = len(line)
    cursor = 0
    while cursor < n:
        while cursor < n and not line[cursor].isdigit() : cursor += 1
        j = cursor
        to_sum = False
        while j < n and line[j].isdigit(): 
            for di, dj in directions:
                if 0 <= i + di < m and 0 <= j + dj < n and not grid[ i + di][j + dj].isdigit() and grid[i + di][j + dj] != '.':
                    to_sum = True
            j += 1
        if to_sum:
            somme += int(line[cursor: j])
        cursor = j
print(somme)
    
# part 2

gears = defaultdict(list)
for i,line in enumerate(grid):
    n = len(line)
    cursor = 0
    while cursor < n:
        while cursor < n and not line[cursor].isdigit() : cursor += 1
        j = cursor
        is_gear = False
        while j < n and line[j].isdigit(): 
            for di, dj in directions:
                if 0 <= i + di < m and 0 <= j + dj < n and grid[i + di][j + dj] == '*':
                    is_gear = True
                    X, Y = i + di, j + dj
            j += 1
        if is_gear:
            gears[(X,Y)].append(int(line[cursor: j]))
        cursor = j

somme = 0
for gear in gears:
    if len(gears[gear]) == 2:
        n1, n2 = gears[gear]
        somme += n1 * n2
print(somme)