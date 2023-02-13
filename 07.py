tls_test = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn""".split("\n")
ssl_test = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb""".split("\n")

def tls(s):
    ok = False
    b = False
    for i,c in enumerate(s):
        if c=='[': b = True
        elif c==']': b = False
        else:
            if i<4: pass
            if c==s[i-3] and s[i-1]==s[i-2] and c!=s[i-1]:
                if b: return False
                else: ok = True
    return ok

def ssl(ss):
    ss=ss.strip()
    s=ss
    ins,outs = [],[]
    p = s.find('[')
    while p != -1:
        outs.append(s[:p])
        s = s[p+1:]
        q = s.find(']')
        assert(p != -1)
        ins.append(s[:q])
        s = s[q+1:]
        p = s.find('[')
    outs.append(s)
    for si in ins:
        for i in range(2,len(si)):
            if si[i]==si[i-2] and si[i] != si[i-1]:
                aba = si[i-1]+si[i]+si[i-1] # bab->aba
                if any([aba in so for so in outs]):
                    return True
    return False

print(len([x for x in open('07.txt') if tls(x)]))
print(len([x for x in open('07.txt') if ssl(x)]))
