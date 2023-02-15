import hashlib

def solve(stretch=0):
    trips = []
    quins = []
    jump = 1000
    for index in range(jump+2):
        tri, qui = gen_next(len(trips), stretch)
        trips.append(tri)
        quins.append(qui)
    keys = []
    index = 0
    while len(keys) < 64:
        trip = trips[index]
        if trip is not None and trip in quins[index+1:index+jump]:
            keys.append(index)
        tri, qui = gen_next(len(trips), stretch)
        trips.append(tri)
        quins.append(qui)
        index += 1
    print(keys[-1])


def gen_next(index, stretch):
    salt = 'jlmsuwbz' #'abc'
    h = hashlib.md5('{}{}'.format(salt,index).encode('utf-8')).hexdigest()
    for _ in range(stretch):
        h = hashlib.md5(h.encode('utf-8')).hexdigest()
    triple = None
    quintl = None
    for i,c in enumerate(h):
        if i>=2 and c==h[i-1] and c==h[i-2]:
            if triple is None: triple = c
            if i>=4 and c==h[i-3] and c==h[i-4]:
                if quintl is None:
                    quintl = c
                    break
    return (triple, quintl)

solve()
solve(2016)
