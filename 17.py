import hashlib

def adjacents(path, p):
    h = hashlib.md5(path.encode('utf-8')).hexdigest()
    ok = [c in 'bcdef' for c in h[:4]]

    x,y = p
    a = []
    if ok[0] and y>0: a.append( ('U',(x,y-1)) )
    if ok[1] and y<3: a.append( ('D',(x,y+1)) )
    if ok[2] and x>0: a.append( ('L',(x-1,y)) )
    if ok[3] and x<3: a.append( ('R',(x+1,y)) )
    return [(path+x[0], x[1]) for x in a]

def solve(passcode):
    searching_for_one = True
    states = [(len(passcode), passcode, (0,0))]
    while states:
        _, path, p = states.pop(0)
        if p==(3,3):
            if searching_for_one:
                searching_for_one = False
                print(path[len(passcode):])
            longest = len(path)-len(passcode)
            continue # Dead end
        for npath, np in adjacents(path, p):
            states.append( (len(npath), npath, np) )
        states.sort()
    print(longest)

solve('ihgpwlah')
solve('kglvqrro')
solve('ulqzkmiv')
solve('njfxhljp')
