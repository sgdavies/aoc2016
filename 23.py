def regix(c):
    # convert character to index in register array
    return ord(c)-ord('a')

def solve(ins, a=0):
    reg = [a,0,0,0]
    ip = 0
    while 0 <= ip < len(ins):
        instr = ins[ip]
        #print(ip, instr)
        words = instr.split()
        if words[0]=="nop":
            pass
        elif words[0]=="mult":
            r1 = regix(words[1])
            r2 = regix(words[2])
            r3 = regix(words[3])
            reg[r1] = reg[r2]*reg[r3]
            reg[r2] = 0
            reg[r3] = 0
        elif words[0]=="mvadd": # add r1 to r2, leaving 0 in r1
            r1 = regix(words[1])
            r2 = regix(words[2])
            reg[r2] += reg[r1]
            reg[r1] = 0
        elif words[0]=="tgl":
            x = words[1]
            val = int(x) if x[0]=='-' or x.isdigit() else reg[regix(x)]
            if not 0 <= ip+val < len(ins):
                ip+= 1
                continue
            tgl_instr = ins[ip+val]
            #print("tgl:",ip+val,tgl_instr)
            tgl_words = tgl_instr.split()
            if tgl_words[0] == "inc":
                tgl_words[0] = "dec"
            elif tgl_words[0] in ["dec","tgl"]:
                tgl_words[0] = "inc"
            elif tgl_words[0] == "jnz":
                tgl_words[0] = "cpy"
            elif tgl_words[0] == "cpy":
                tgl_words[0] = "jnz"
            else:
                print("Unexpected toggle instruction:", tgl_instr)
                exit(1)
            ins[ip+val] = " ".join(tgl_words)
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

test_instructions = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a""".split("\n")
#solve(test_instructions)

#instructions = [l.strip() for l in open('23.txt')]
#solve(list(instructions), a=7)

# Part two - replace chunks of instructions in the input
# with multiply instructions instead
# See also aoc2021 day 10 commit 3d85d7 for similar optimizations in BF
instructions = [l.strip() for l in open('23_2.txt')]
solve(list(instructions), a=7)
solve(list(instructions), a=12)
