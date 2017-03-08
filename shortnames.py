def replacement(name):


def identify_name(line):
    sub = ''
    if ')' in  line:
        if 'gi:' in line:
            sub = line.split('(')[2].split(')')[0]
        else:
            sub = line[line.find("(")+1:line.find(")")]
    return sub

def enumerate2(xs, start=0, step=1):
    for x in xs:
        yield (start, x)
        start += step

def shortnames(fname='data/repaired_ecoli_vfs.ffn'):
    lines = []
    with open(fname) as f:
        lines = [line.rstrip('\n') for line in f]

    for i, l in enumerate(lines):


    for ip, p in enumerate(lines):
        subp = identify_name(lines[ip])
        subp = subp.split('_')[0]
        for iq, q in enumerate(lines[ip+1:]):
            subq = identify_name(lines[iq])
            subq = subq.split('_')[0]
            if (subp.lower() in subq.lower()) or (subq.lower() in subp.lower()):
                if len(subp) > len(subq):
                    lines[ip] = lines[ip].replace(subp,subq,1)
                elif len(subp) < len(subq):
                    lines[iq] = lines[iq].replace(subq,subp,1)

    p=0
    while p<len(lines)-1-2:
        subp = identify_name(lines[p])
        subp = subp.split('_')[0]
        q=p
        p += 2
        while q<len(lines)-1:
            subq = identify_name(lines[q])
            subq = subq.split('_')[0]
            if (subp.lower() in subq.lower()) or (subq.lower() in subp.lower()):
                if len(subp) > len(subq):
                    lines[ip] = lines[ip].replace(subp,subq,1)
                elif len(subp) < len(subq):
                    lines[iq] = lines[iq].replace(subq,subp,1)


    for i1, row1 in hits.iterrows():
        subframe = hits.loc[hits.index>i1]
        for i2, row2 in subframe.iterrows():
            if (row1.hitname.lower() in row2.hitname.lower()) or (row2.hitname.lower() in row1.hitname.lower()):
                if len(row1.hitname) > len(row2.hitname):
                    hits.loc[i1,'hitname']=row2.hitname
                elif len(row1.hitname) < len(row2.hitname):
                    hits.loc[i2, 'hitname']=row1.hitname
    return hits



if __name__ == '__main__':
    shortnames()
