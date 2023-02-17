lines = [line for line in open('22.txt')][2:]
import re
re_node = re.compile("/dev/grid/node-x([0-9]+)-y([0-9]+)\s+([0-9]+)T\s+([0-9]+)T\s+([0-9]+)T\s+([0-9]+)%")

#nodes: (0=x, 1=y, 2=size, 3=used, 4=avail)
nodes = []
for line in lines:
    if m := re_node.match(line):
        #nodes.append( tuple(int(m.group(n)) for n in [1,2,3,4,5]) )
        nodes.append( list(int(m.group(n)) for n in [1,2,3,4,5]) )
    else:
        print("Bad regex:",line)
        exit(1)

count = 0
for ix in range(len(nodes)-1):
    for jx in range(ix+1,len(nodes)):
        na = nodes[ix]
        nb = nodes[jx]
        if na[3]>0 and na[3] <= nb[4]: count +=1
        if nb[3]>0 and nb[3] <= na[4]: count +=1

print(count)

# Part two
EMPTY='_'
TILE='.'
BLOCK='#'
GOAL='G'
#grid: keyed by (x,y). Items are EMPTY (1x), TILE (small disk) and BLOCK
grid = {}
ngrid = {}

for node in nodes:
    if node[3]==0: tile = EMPTY
    elif node[2]<100: tile = TILE
    else: tile = BLOCK
    grid[(node[0],node[1])] = tile
    ngrid[(node[0],node[1])] = node

xmax = max([n[0] for n in nodes])
ymax = max([n[1] for n in nodes])
#print(xmax,ymax)
grid[(xmax,0)] = GOAL
def pg(): print("\n".join(["".join([grid[(x,y)] for x in range(xmax+1)]) for y in range(ymax+1)]))
# By inspection - 129 steps.  But that's too low.
# 34 L, 27 U, 33 R, 35 L
# ** Answer ** - because the final "35 L" is not correct. Have to do a 'shuffle'
# as explained in the block comment further down.
# The rest of the code below is overkill for the actual answer, which is:
# print(34+27+33+ 1 +34*5)
# -- the code was used to check this more thoroughly.
def find(tile):
    for x in range(xmax+1):
        for y in range(ymax+1):
            if grid[(x,y)]==tile: return x,y
gMoves = 0
def move(pa,pb):
    global gMoves
    na = ngrid[pa]
    nb = ngrid[pb]
    if nb[4] < na[3]:
        pg()
        print("Illegal move",na,nb)
        exit()
    else:
        gMoves += 1
        nb[4] -= na[3]
        nb[3] += na[3]
        na[4] += na[3]
        na[3] = 0
        t = grid[pa]
        grid[pa] = grid[pb]
        grid[pb] = t

px,py = find(EMPTY)
for s1 in range(34):
    move( (px-1-s1,py),(px-s1,py) )
assert find(EMPTY) == (1,py)
for s2 in range(27):
    move( (1,py-1-s2),(1,py-s2) )
assert find(EMPTY) == (1,0)
for s3 in range(33):
    move( (1+s3+1,0),(1+s3,0) )
assert find(EMPTY) == (34,0)
gx,gy = find(GOAL)
while True:
    # ...._G..
    # ........
    # Need to: move G L
    #          move G(+1,+1) up
    #          move G(0,+1) R
    #          move G(-1,+1) R
    #          move G(-1,0) D
    move((gx,gy), (gx-1,gy))
    gx -= 1
    if (gx,gy)==(0,0):
        break
    move( (gx+1,gy+1),(gx+1,gy) )
    move( (gx,gy+1),  (gx+1,gy+1) )
    move( (gx-1,gy+1),(gx,gy+1) )
    move( (gx-1,gy),  (gx-1,gy+1) )
assert find(EMPTY) == (1,0)
assert find(GOAL) == (0,0)
#print(ngrid[(0,0)])
print("Moves:", gMoves)
