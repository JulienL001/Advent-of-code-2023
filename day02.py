import collections
import numpy as np

file = open('day02.txt', 'r', encoding='utf-8-sig')
lines = file.read().splitlines()
# lines ='''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''.splitlines()
# directions = {'>': (1,0), '^':(0,1), '<':(-1,0), 'v':(0,-1)}
# directions = [(1,0), (0,1), (-1,0), (0,-1)]
# L = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# visited = set()
# d = collections.defaultdict(int)

# part 1
somme = 0
max_r = 12
max_g = 13
max_b = 14
for line in lines:
    L = line.split(':')
    possible = True
    P = L[1].split(';')
    for z in P: 
        l=z.split()
        r, g, b = 0, 0, 0
        for i,e in enumerate(l):
            if e.isnumeric():
                if 'red' in l[i+1]:r+=int(e)
                if 'green' in l[i+1]:g+=int(e)
                if 'blue' in l[i+1]:b+=int(e)
        if r > max_r or g > max_g or b > max_b: 
            possible = False     
    if possible:
        somme += int(L[0].split()[1])    
print(somme)
    
# part 2

somme = 0
for line in lines:
    L = line.split(':')
    P = L[1].split(';')
    r, g, b = 0, 0, 0
    for z in P: 
        l=z.split()
        for i,e in enumerate(l):
            if e.isnumeric():
                if 'red' in l[i+1]:
                    if r<int(e): r= int(e)
                if 'green' in l[i+1]:
                    if g<int(e): g= int(e)
                if 'blue' in l[i+1]:
                    if b<int(e): b= int(e)
    somme += r*g*b    
print(somme)