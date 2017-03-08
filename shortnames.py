def identify_name(line):
    sub = ''
    if ')' in  line:
        if 'gi:' in line:
            sub = line.split('(')[2].split(')')[0]
        else:
            sub = line[line.find("(")+1:line.find(")")]
    return sub

def weird_name(subq,subp):
    '''
    returns true if either value is a weird name and short be ignored
    '''
    t = ('st','tia')
    return (subq in t) or (subp in t)

def shortnames(fname='data/repaired_ecoli_vfs.ffn'):
    lines = []
    with open(fname) as f:
        lines = [line.rstrip('\n') for line in f]

    for i in range(0,len(lines),2):
        sub = identify_name(lines[i])
        stri = sub.split('_')[0].split('-I')[0].split('-V')[0]
        if sub != stri:
            if '-I' in stri:
                stri.split('-I')[0]
            lines[i] = lines[i].replace(sub,stri,1)

    p=0
    while p<len(lines)-1-2:
        subp = identify_name(lines[p])
        q=p
        while q<len(lines)-1:
            subq = identify_name(lines[q])
            if ((subp.lower() in subq.lower()) or (subq.lower() in subp.lower())) and not weird_name(subq, subp):
                if len(subp) > len(subq):
                    lines[p] = lines[p].replace(subp,subq,1)
                elif len(subp) < len(subq):
                    lines[q] = lines[q].replace(subq,subp,1)
            q += 2
        p += 2

    with open('data/repaired_ecoli_vfs_shortnames.ffn', 'w') as f:
        for line in lines:
            f.write(line + '\n')

if __name__ == '__main__':
    shortnames()
