import re
re_room = re.compile(r"([-a-z]+)-([0-9]+)\[([a-z]+)\]")
rooms = []
test_lines = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
qzmt-zixmtkozy-ivhz-343[zimth]""".split("\n")

part_two = None
#for line in test_lines:
for line in open('04.txt'):
    if m := re_room.match(line):
        encr_name = m.group(1)
        sector_id = int(m.group(2))
        checksum = m.group(3)
        counts = {}
        for c in encr_name:
            if c != '-':
                if c not in counts: counts[c]=0
                counts[c] += 1
        fkey = lambda c: counts[c] - ord(c)/100
        real_checksum = "".join(sorted(counts.keys(), key=fkey, reverse=True)[:5])
        real = checksum==real_checksum
        rooms.append((encr_name, sector_id, checksum, real_checksum, real))
        if real:
            name = "".join([' ' if c=='-' else chr(ord('a')+ ((ord(c)+sector_id-ord('a'))%26)) for c in encr_name])
            if "orth" in name: part_two = sector_id
    else:
        print("regex didn't match:", line)
        exit(1)

print(sum([r[1] for r in rooms if r[-1]]))
print(part_two)
