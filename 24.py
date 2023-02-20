def solve(lines, back_to_start=False):
    grid = {}
    allnums = ""
    num_pos = {}
    for row,line in enumerate(lines):
        for col, c in enumerate(line):
            if c in '.0123456789': grid[(row,col)] = c
            if c in '0123456789':
                allnums += c
                num_pos[c] = (row,col)
    allnums = set(allnums)
    allnums.remove('0')

    dists = get_dists(grid, num_pos)

    states = [ (0, '0', allnums) ]
    while states:
        steps, pos, keys_left = states.pop(0)

        done = False
        if not keys_left:
            if back_to_start:
                keys_left.add('0')
                keys_left.add('X')
            else:
                done = True
        elif keys_left == set('X'):
            done = True

        if done:
            print(steps)
            return

        for key in [k for k in keys_left if k!='X']:
            nkleft = set(keys_left)
            nkleft.remove(key)
            nsteps = steps + dists[pos][key]
            states.append( (nsteps, key, nkleft) )

        states.sort()

def get_dists(grid, np):
    # find all distances between all pairs of numbers
    dists = {}
    for key, start in np.items():
        dists[key] = dijk(start, grid)
    return dists

INF = 1000000000
def dijk(start, grid):
    dist = {p:INF for p in grid}
    dist[start] = 0
    Q = set(grid.keys())
    while Q:
        u = sorted([q for q in Q], key=lambda p: dist[p])[0]
        Q.remove(u)
        for v in [n for n in neighbours(u) if n in Q]:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
    dists = {}
    for k,v in dist.items():
        c = grid[k]
        if c.isdigit():
            dists[c] = v
    return dists

def neighbours(p):
    r,c = p
    return [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]

test_lines = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########""".split("\n")

solve(test_lines)

lines = [line.strip() for line in open('24.txt')]
solve(lines)
solve(lines, True)
