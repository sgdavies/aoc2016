ODFN = 1362
space_cache = {}
def space( p ):
    if p not in space_cache:
        x,y = p
        val = x*x + 3*x + 2*x*y + y + y*y + ODFN
        c = 0
        while val:
            c += val&1
            val >>= 1
        space_cache[p] = (c%2==0)
    return space_cache[p]

#print("\n".join(["".join(['.' if space( (x,y) ) else '#' for x in range(10)]) for y in range(10)]))

def neighbours(p):
    a = []
    for d in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx = p[0]+d[0]
        ny = p[1]+d[1]
        if nx>=0 and ny>=0:
            a.append( (nx,ny) )
    return a

# Need A* algorithm - because the grid is infinite
def solve(target):
    start = (1,1)
    visited = set()
    part_one = None
    part_two = None

    active = [ (0, start) ]
    while part_one is None or part_two is None:
        steps, p = active.pop(0)
        if p==target: part_one = steps
        if part_two is None and steps>50: part_two = len(visited)
        visited.add(p)
        for np in neighbours(p):
            if np not in visited and space(np):
                active.append( (steps+1, np) )
        active.sort()

    print(part_one)
    print(part_two)

solve((31,39))
