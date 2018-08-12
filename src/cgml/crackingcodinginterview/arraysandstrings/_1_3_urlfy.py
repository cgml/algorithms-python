def urlfy(str):
    lstr = list(str)
    lastidx = len(lstr)-1
    while lastidx >=0:
        if lstr[lastidx] != ' ': break
        lastidx-=1
    spaces = sum([1 for s in lstr[:lastidx] if s == ' '])
    idx = lastidx
    while idx >=0 and spaces >0:
        if lstr[idx] != ' ': lstr[idx+spaces*2]=lstr[idx]
        else:
            spaces-=1
            lstr[idx+spaces*2], lstr[idx+spaces*2+1], lstr[idx+spaces*2+2]='%','2','0'
        idx-=1
    return "".join(lstr)

print(urlfy("l addy   gaga                 "))
print(urlfy("l a d d y g a g a                 "))


