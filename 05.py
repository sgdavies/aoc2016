import hashlib

index=0
door='wtnhxymk'
out = ""
out2= [None for _ in range(8)]
while True:
    h = hashlib.md5('{}{}'.format(door,index).encode('utf-8')).hexdigest()
    if h[:5] == '00000':
        if len(out) < 8: out += h[5]

        p,c = h[5],h[6]
        if '0'<=p<='7':
            ix = int(p)
            if out2[ix] is None:
                out2[ix] = c
                print("".join([c if i==ix else '.' for i in range(8)]))
                if all([x is not None for x in out2]):
                    break
    index += 1

print(out)
print("".join(out2))
