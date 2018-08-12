'''
match +1
missmatch -mu (e.g. mu = 0
insert/delete -sigma ( e.g -1)

common subsequence - matches

Alignment:
    score = #matches - mu * #mismatches - sigma * #indel

    Input: strings, mu, sigma
    Output: alignment maximizing score

Common subsequence problems:
    - Common longest subsequence (max score with mu=sigma=0)

Edit distance: find minimal number of operations to create equal string
    - minimizing edit distance is the same as maximizing alignment score

'''
import numpy as np

def edit_distance_matrix(a,b):
    row_len = len(a)+1
    col_len = len(b)+1
    mem = np.zeros((row_len,col_len), dtype=np.int32)
    for idrow in range(row_len): mem[idrow][0]=idrow
    for idcol in range(col_len): mem[0][idcol]=idcol
    for j in range(1,col_len):
        for i in range(1,row_len):
            insertion = mem[i][j-1] + 1
            deletion = mem[i-1][j] + 1
            match_mismatch = mem[i-1][j-1] if a[i-1] == b[j-1] else mem[i-1][j-1]+1
            mem[i][j]=min(insertion,deletion,match_mismatch)
    return mem

def edit_distance(a,b):
    return edit_distance_matrix(a,b)[-1][-1]

def backtrack(mem,i,j):
    print(i,j, mem.shape)
    if j > 0: insert = mem[i][j]-mem[i][j-1]
    else: insert = 2

    if i > 0: delete = mem[i][j]-mem[i-1][j]
    else: delete = 2

    if i > 0 and j > 0: mis_match = mem[i][j]-mem[i-1][j-1]
    else: mis_match = 2

    idx = np.argmin(np.array([insert,delete,mis_match]))
    return ['insert', 'delete', 'match/mismatch'][idx]


def optimal_alignment_backtrack(a,b,i,j, mem, output):
    if i<=0 and j<=0: return output
    if i > 0 and mem[i,j] == mem[i-1,j]+1:
        output[0].append(a[i-1])
        output[1].append('-')
        optimal_alignment_backtrack(a,b,i-1,j, mem, output)
    elif j > 0 and mem[i,j] == mem[i,j-1] + 1:
        output[0].append('-')
        output[1].append(b[j-1])
        optimal_alignment_backtrack(a,b,i,j-1, mem, output)
    else:
        if i>0: output[0].append(a[i-1])
        else: output[0].append('-')
        if j>0: output[1].append(b[j-1])
        else: output[1].append('-')
        optimal_alignment_backtrack(a,b,i-1,j-1, mem, output)
    return output

def optimal_allignment(a,b):
    mem = edit_distance_matrix(a,b)
    output = optimal_alignment_backtrack(a,b,len(a),len(b), mem,[[],[]])
    output[0].reverse()
    output[1].reverse()
    print(output[0])
    print(output[1])
    return output

assert edit_distance("editing","string") == 4
assert edit_distance("editing","edditing") == 1
assert optimal_allignment('editing','distance') == [ ['e', 'd', 'i', '-', 't', 'i', 'n', 'g', '-'], ['-', 'd', 'i', 's', 't', 'a', 'n', 'c', 'e'] ]
assert optimal_allignment('ddddistance','distance') == [['d', 'd', 'd', 'd', 'i', 's', 't', 'a', 'n', 'c', 'e'], ['d', '-', '-', '-', 'i', 's', 't', 'a', 'n', 'c', 'e']]