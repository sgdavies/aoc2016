test_lines = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2""".split("\n")
lines = [line.strip() for line in open('10.txt')]
#lines = test_lines
part_one_bot = [17,61]

bots = {}
outs = {}

def get_bot(id):
    if id not in bots: bots[id] = []
    return bots[id]

while lines:
    next_lines = []
    for line in lines:
        words = line.split()
        if words[0] == "value":
            bot_id = words[-1]
            get_bot(bot_id).append(int(words[1]))
        else:
            fromb = get_bot(words[1])
            if len(fromb) == 2:
                tolo = words[6]
                tohi = words[-1]
                if sorted(fromb) == part_one_bot:
                    print(words[1])
                    #exit()
                lo = min(fromb)
                hi = max(fromb)
                if words[5] == "output": outs[tolo] = lo
                else: get_bot(tolo).append(lo)
                if words[10] == "output": outs[tohi] = hi
                else: get_bot(tohi).append(hi)
            else:
                next_lines.append(line)

    lines = next_lines

#print(outs)
print(outs['0']*outs['1']*outs['2'])
