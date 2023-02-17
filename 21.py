def solve(password, lines, reverse=False):
    pwd = [c for c in password]
    if reverse: lines.reverse()

    for line in lines:
        words = line.strip().split()
        if words[0]=="swap":
            # unaffected by going backwards
            if words[1]=="letter":
                lx = words[2]
                ly = words[5]
                px = pwd.index(lx)
                py = pwd.index(ly)
                assert(px<len(pwd) and py<len(pwd))
            else:
                px = int(words[2])
                py = int(words[5])
            t = pwd[px]
            pwd[px] = pwd[py]
            pwd[py] = t
        elif words[0]=="rotate":
            if words[1]=="based":
                if reverse:
                    for t in range(len(pwd)):
                        tpwd = pwd[t:]+pwd[:t]
                        if based_rotate(tpwd,words[6])==pwd:
                            ans = tpwd
                            break
                    pwd = ans
                else:
                    pwd = based_rotate(pwd,words[6])
            else:
                if words[1]=="left":
                    r = -int(words[2])
                elif words[1]=="right":
                    r = int(words[2])

                if reverse: r = -r
                r %= len(pwd)
                pwd = pwd[-r:] + pwd[:-r]
        elif words[0]=="reverse":
            # unaffected by going backwards
            px = int(words[2])
            py = int(words[4])
            mid = pwd[px:py+1]
            mid.reverse()
            pwd = pwd[:px]+mid+pwd[py+1:]
        elif words[0]=="move":
            px = int(words[2])
            py = int(words[5])
            if reverse: px,py = py,px
            a = pwd[px]
            pwd = pwd[:px]+pwd[px+1:]
            pwd = pwd[:py]+[a]+pwd[py:]
        else:
            print("Unexpected instruction", line)
            assert False

    print("".join(pwd))

def based_rotate(a,c):
    px = a.index(c)
    r = 1+px
    if px>=4: r+=1
    r %= len(a)
    return a[-r:] + a[:-r]

test_lines = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d""".split("\n")

#solve("abcde", test_lines)
#solve("decab", test_lines, True)
solve("abcdefgh", [line for line in open('21.txt')])
solve("fbgdceah", [line for line in open('21.txt')], True)
