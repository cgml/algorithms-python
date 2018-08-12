from cgimaster.crackingcodinginterview.treesandgraphs._0_toolset import *
from cgimaster.crackingcodinginterview.treesandgraphs._4_2_bst_from_sorted_array import *

def listofdepth(n,d=0,l=[]):
    if not n: return l
    while len(l)<=d:l+=[[]]
    l[d].append(n)
    listofdepth(n.l,d+1,l)
    listofdepth(n.r,d+1,l)
    return l


lists = listofdepth(bst(sorted([1, 10, 11, 2, 3, 33, 7, 23, 24, 12])))
for idx, l in enumerate(lists):
    print('\n',idx+1,':',end='')
    for n in l: print(n.v,end=' ')
