import math
from sortedcontainers import SortedSet

def check_floor(f):
    nchips = [c for c in f if c.islower()]
    ngens = [c for c in f if c.isupper()]
    if not nchips or not ngens:
        return True # no mixed - this is fine

    for nc in nchips:
        if not nc.upper() in ngens:
            return False
    return True

def lower_bound(floors):
    # minimum possible steps to get all items to the top floor
    # ignore elevator position
    # go floor by floor. Can carry 2 up at a time, but if there
    # are still some left then have to return with 1 and then repeat.
    # So 1 item up 1 floor -> 1 step, 2->1 step, 3->3, 4->5, 5->7 etc
    prev = ""
    s = 0
    for i in range(len(floors)-1):
        f = prev+floors[i]
        if len(f)==1: s+=1
        else: s += 2*(len(f)-1) -1
        prev = f
    return s

def normalize(floors):
    # ["Aa", "Bb", ...] is equivalent to ["Bb", "Aa", ...]
    # Normalize what gets put into seen_states to
    # massively reduce search space.
    # Sort by floor and by (pairs, generators, chips)
    # So ["WwXYz","x","y","Z"] -> ["AaBCd","b","c","D"]
    # because Ww is a pair on floor 1; then XY are gens where
    # x is on a lower floor than y; then Z is the only one left
    # Of course "WwXYz" is equivalent to "XzwYW" etc.
    norm_floors = ["","","",""]
    m = {}
    cx = ord('A')
    for i, floor in enumerate(floors):
        pgc = ["","",""] # pairs, gens, chips
        seen = ""
        for c in floor:
            if c in seen: continue
            if c.upper() in m:
                if c.isupper():
                    norm_floors[i] += m[c]
                else:
                    norm_floors[i] += m[c.upper()].lower()
            else:
                seen += c
                if c.isupper():
                    if c.lower() in floor:
                        seen += c.lower()
                        pgc[0] += c
                    else:
                        pgc[1] += c
                else:
                    if c.upper() in floor:
                        seen += c.upper()
                        pgc[0] += c.upper()
                    else:
                        pgc[2] += c
        for c in pgc[0]:
            nc = chr(cx)
            cx += 1
            m[c] = nc
            norm_floors[i] += nc + nc.lower()
        for c in pgc[1]:
            nc = chr(cx)
            cx += 1
            m[c] = nc
            norm_floors[i] += nc
        for c in pgc[2]:
            nc = chr(cx)
            cx += 1
            m[c.upper()] = nc
            norm_floors[i] += nc.lower()
    return norm_floors

if False:  # Tests of the normalize() function
    print('["Xx","Bb","",""] -> ["Bb","Aa","",""]')
    print(normalize(["Xx","Ff","",""]))
    print(normalize(["xX","Ff","",""]))
    print(normalize(["Yy","Xx","",""]))
    print("WwX,x -> AaB,b")
    print(normalize(["WwX","x","",""]))
    print('["WwXYz","x","y","Z"] -> ["AaBCd","b","c","D"]')
    print(normalize(["WwXYz","x","y","Z"]))
    print(normalize(["XzwYW","x","y","Z"]))
    print(normalize(["XzwYW","y","x","Z"]))
    exit()

def solve(floors):
  elevator = 0
  steps = 0
  states = SortedSet()
  states.add( (steps+lower_bound(floors), steps, elevator, tuple(floors)) )
  seen_states = set(); seen_states.add(tuple([elevator]+normalize(floors)))
  while True:
    _,s,e,fl = states.pop(0)
    #print(e, " # ".join(fl), "\t",len(states),"\t",len(seen_states))
    if all([f=="" for f in fl[:3]]):
        #print(fl)
        return s

    # what can I pick up on this floor?
    # all combinations of 1 or 2 items
    # then trim based on (1) what's in the elevator and (2) what's left behind
    # ... but not (1) - it only says if left "in the same area" they will be
    # fried -- do we assume this means travelling in the elevator is OK?
    to_check = [] # all possible combos
    tf = fl[e] # this floor
    for i in range(len(tf)):
        to_check.append( (tf[i], tf.replace(tf[i],'')) )
        for j in range(i+1, len(tf)):
            to_check.append( (tf[i]+tf[j], tf.replace(tf[i],'').replace(tf[j],'')) )
    to_go = [] # combos that leave the current floor in a valid state
    for tc in to_check:
        if check_floor(tc[1]):
            to_go.append(tc)
    new_elevators = []
    if e > 0: new_elevators.append(e-1)
    if e < 3: new_elevators.append(e+1)
    for ne in new_elevators:
        for tc in to_go:
            if check_floor(fl[ne]+tc[0]):
                new_floors = list(fl)
                new_floors[e] = tc[1]
                new_floors[ne] = fl[ne]+tc[0]
                seen_key = tuple([ne]+normalize(new_floors))
                if seen_key not in seen_states:
                    states.add( (s+1+lower_bound(new_floors), s+1, ne, tuple(new_floors)) )
                    seen_states.add(seen_key)

floors = ["TtPS","ps","MmRr",""] # pro[M]ethium, [P]lutonium
# test data:
#floors = ["hl","H","L",""]     # 11,   0.03s
#floors = ["TtPS","ps","",""]   # 23,   0.60s
#floors = ["TtPS","ps","Mm",""] # 27, 468   s  New:  40 s
#floors = ["TtPS","ps","MmRr",""] # 31, (real data)  3 hours

## Time much sped up by 2 major enhancements:
## 1. Tighter lower bound -> better A* algorithm
## 2. Adding normalize() to remove equivalent states
print(solve(floors))

floors[0] += "EeDd"
print(solve(floors))
exit()

