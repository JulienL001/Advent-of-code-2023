# import collections
# import numpy as np

file = open('day01.txt', 'r', encoding='utf-8-sig')
lines = file.read().splitlines()

# directions = {'>': (1,0), '^':(0,1), '<':(-1,0), 'v':(0,-1)}
# directions = [(1,0), (0,1), (-1,0), (0,-1)]
# visited = set()

# part 1
S=0
for line in lines:
    s = ''
    for c in line:
        if c.isdigit():
            s+=c
            break
    for c in line[::-1]:
        if c.isdigit():
            s+=c
            break
    S+=int(s)
print(S)

# part 2
L = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
S=0
for line in lines:
    s = ''
    for i,c in enumerate(line):
        if c.isdigit():
            s+=c
            break
        for j,u  in enumerate(L):
            if line[i:].startswith(u):
                s+=str(j)
                break
        if len(s)==1:break
    for i in range(len(line)):
        c = line[len(line)-1-i]
        if c.isdigit():
            s+=c
            break
        for j,u  in enumerate(L):
            if line[len(line)-1-i:].startswith(u):
                s+=str(j)
                break
        if len(s)==2:break
    print(s)
    S+=int(s)
print(S)