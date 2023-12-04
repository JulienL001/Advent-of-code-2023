from collections import defaultdict
from itertools import product, combinations, permutations
import numpy as np

file = open('day04.txt', 'r', encoding='utf-8-sig')
lines = file.read().splitlines()
# grid = file.read().splitlines()
# lines ='''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.splitlines()
# directions = {'>': (1,0), '^':(0,1), '<':(-1,0), 'v':(0,-1)}
# directions = [(1,0), (0,1), (-1,0), (0,-1)]
# directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)] # all directions around
# L = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# visited = set()
# d = defaultdict(int)
# m, n = len(grid), len(grid[0])


# part 1
somme = 0
for i, line in enumerate(lines):
    s = 0
    a, numbers = line.split(': ')
    numbers1, numbers2 = numbers.split('|')
    l1 = list(map(int, numbers1.split()))
    l2 = list(map(int, numbers2.split()))
    for n in l1:
        if n in l2:
            s +=1
    if s > 0:
        somme += 2**(s-1)
print(somme)
    
# part 2

num_copies = [1 for i in range(len(lines))]
for i, line in enumerate(lines):
    s = 0
    a, numbers = line.split(': ')
    numbers1, numbers2 = numbers.split('|')
    l1 = list(map(int, numbers1.split()))
    l2 = list(map(int, numbers2.split()))
    for n in l1:
        if n in l2:
            s +=1
    for j in range(i+1, i+1+s):
        if j < len(num_copies):
            num_copies[j] += num_copies[i]
        somme += j*2**(s-1)
print(sum(num_copies))
