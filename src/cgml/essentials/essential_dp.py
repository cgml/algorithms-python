import numpy as np

def edit_distance_matrix(s1,s2):
    R, C = len(s1)+1, len(s2)+1
    mem = np.zeros((R, C))
    for r in range(R): mem[r][0]=r
    for c in range(C): mem[0][c]=c

    for c in range(1,C):
        for r in range(1,R):
            insertion = mem[r][c-1]+1
            deletion = mem[r-1][c]+1
            match_mismatch = mem[r-1][c-1] if s1[r-1] == s2[c-1] else mem[r-1][c-1]+1
            mem[r][c] = min(insertion, deletion, match_mismatch)
    return mem


def edit_distance(s1, s2):
    return edit_distance_matrix(s1,s2)[-1][-1]

def optimal_alignment_backtrack(s1,s2,R,C, mem, output):
    if R <= 0 and C <= 0: return output
    if R > 0 and mem[R][C] == mem[R-1,C]+1:
        output[0].append(s1[R-1])
        output[1].append('-')
        optimal_alignment_backtrack(s1,s2,R-1,C,mem,output)
    elif C > 0 and mem[R][C] == mem[R,C-1]+1:
        output[0].append('-')
        output[1].append(s2[C-1])
        optimal_alignment_backtrack(s1,s2,R,C-1,mem,output)
    else:
        if R > 0: output[0].append(s1[R-1])
        else: output[0].append('-')
        if C > 0: output[1].append(s2[C-1])
        else: output[1].append('-')
        optimal_alignment_backtrack(s1, s2, R - 1, C - 1, mem, output)
    return output

def optimal_allignment(s1, s2):
    mem = edit_distance_matrix(s1,s2)
    output = optimal_alignment_backtrack(s1,s2,len(s1),len(s2), mem,[[],[]])
    output[0].reverse()
    output[1].reverse()
    print(output[0])
    print(output[1])
    return output


assert edit_distance("editing", "string") == 4
assert edit_distance("editing", "edditing") == 1
assert optimal_allignment('editing', 'distance') == [['e', 'd', 'i', '-', 't', 'i', 'n', 'g', '-'], ['-', 'd', 'i', 's', 't', 'a', 'n', 'c', 'e']]
assert optimal_allignment('ddddistance', 'distance') == [['d', 'd', 'd', 'd', 'i', 's', 't', 'a', 'n', 'c', 'e'], ['d', '-', '-', '-', 'i', 's', 't', 'a', 'n', 'c', 'e']]

#
# Coin change problem

# def change_dp_count(target,denoms):
#     minnums = [0]*(target+1)
#     for m in range(1,target+1):
#         minnums[m]=target*target # =~ infinity
#         for coin in denoms:
#             if m >= coin:
#                 numcoins = minnums[m-coin] + 1
#                 if numcoins < minnums[m]: minnums[m]=numcoins
#     return minnums[target]
#
#
# def change_dp(target,denoms):
#     minnums = [[]]*(target+1)
#     for m in range(1,target+1):
#         minnums[m]=[1]*target # =~ infinity. assume we have coin with denom 1
#         for coin in denoms:
#             if m >= coin:
#                 numcoins = minnums[m-coin] + [coin]
#                 if len(numcoins) < len(minnums[m]): minnums[m]=numcoins
#     return minnums[target]
#

def change_dp_count(target, denoms):
    mem = [0]*(target+1)
    for idx in range(1,target+1):
        mem[idx] = target
        for coin in denoms:
            if idx >= coin:
                mem[idx] = min(mem[idx],mem[idx-coin]+1)
    return mem[target]

def change_dp(target, denoms):
    mem = [[]]*(target+1)
    for idx in range(1, target+1):
        mem[idx] = [1]*target # sort of infinity - expect that there is coin 1
        for coin in denoms:
            if idx >= coin:
                num = mem[idx-coin]+[coin]
                if len(mem[idx]) > len(num): mem[idx]=num
    return mem[target]


assert change_dp_count(53,[50,25,20,10,5,1]) == 4
assert change_dp(53,[50,25,20,10,5,1]) == [1,1,1,50]
assert change_dp(97,[50,25,20,10,5,1]) == [1, 1, 20, 25, 50]



#
# Knapsack 0/1 no repetitions
def knapsack_norep(W, values, weights):
    mem, NV = np.zeros((W+1,len(values)+1)), len(values)+1
    for c in range(1,NV):
        for w in range(1,W+1):
            mem[w,c]=mem[w,c-1]
            if weights[c-1] <= w:
                mem[w,c] = max(mem[w-weights[c-1], c-1]+values[c-1], mem[w,c])
    return mem[-1][-1]

assert knapsack_norep(10,[30,14,16,9],[6,3,4,2]) == 46
assert knapsack_norep(50,[60, 100, 120],[10, 20, 30]) == 220

