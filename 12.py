def regix(c):
    # convert character to index in register array
    return ord(c)-ord('a')

def solve(ins, c=0):
    reg = [0,0,c,0]
    ip = 0
    while 0 <= ip < len(ins):
        instr = ins[ip]
        words = instr.split()
        if words[0]=="cpy":
            x = words[1]
            y = words[2]
            if x.isdigit():
                val = int(x)
            else:
                val = reg[regix(x)]
            reg[regix(y)] = val
        elif words[0] == "inc":
            reg[regix(words[1])] += 1
        elif words[0] == "dec":
            reg[regix(words[1])] -= 1
        elif words[0] == "jnz":
            t = words[1]
            if t.isdigit():
                val = int(t)
            else:
                val = reg[regix(t)]
            if val:
                ip += int(words[2])
                ip -= 1 # hack since we're about to increment it
        ip += 1
    print(reg[0])

instructions = [l.strip() for l in open('12.txt')]
solve(instructions)
solve(instructions, c=1)
