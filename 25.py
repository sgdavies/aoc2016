def regix(c):
    # convert character to index in register array
    return ord(c)-ord('a')

def solve(ins, a=0):
    reg = [a,0,0,0]
    ip = 0
    out = []
    while 0 <= ip < len(ins):
        instr = ins[ip]
        #print(ip, instr)
        words = instr.split()
        if words[0]=="nop":
            pass
        elif words[0]=="out":
            v = reg[regix(words[1])]
            if v not in [0,1]: return False
            if out and out[-1] != (v+1)%2: return False
            out.append(v)
            if len(out) > 10: return True
        elif words[0]=="mult":
            r1 = regix(words[1])
            r2 = regix(words[2])
            r3 = regix(words[3])
            reg[r1] = reg[r1] + reg[r2]*reg[r3]
            reg[r2] = 0
            reg[r3] = 0
        elif words[0]=="mvadd": # add r1 to r2, leaving 0 in r1
            r1 = regix(words[1])
            r2 = regix(words[2])
            reg[r2] += reg[r1]
            reg[r1] = 0
        elif words[0]=="cpy":
            x = words[1]
            y = words[2]
            val = int(x) if x[0]=='-' or x.isdigit() else reg[regix(x)]
            reg[regix(y)] = val
        elif words[0] == "inc":
            reg[regix(words[1])] += 1
        elif words[0] == "dec":
            reg[regix(words[1])] -= 1
        elif words[0] == "jnz":
            t = words[1]
            val = int(t) if t[0]=='-' or t.isdigit() else reg[regix(t)]
            if val:
                t = words[2]
                val = int(t) if t[0]=='-' or t.isdigit() else reg[regix(t)]
                ip += val
                ip -= 1 # hack since we're about to increment it
        else:
            print("Invalid instruction:", ip, instr)
            exit(1)
        ip += 1
        #print(reg)
    print(reg[0])

instructions = [l.strip() for l in open('25.txt')]
a = 0
while True:
    if solve(instructions, a=a):
        print("Solution!", a)
        exit()
    a += 1
    #if a%100==0: print(a, "...")
