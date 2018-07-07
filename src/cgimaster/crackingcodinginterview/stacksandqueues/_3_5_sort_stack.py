'''
3.5: Write a program to sort stack such that the smallest tiems are on the top.
You can use an additional temporary stack, but you may not copy the elements
into any other data structure such as an array. The stack supports the following operations:
push, pop, peek and isEmpty

Implementation:
TC: O(N^2)
SC: O(N)


For simplicity python lists are used as stacks with following allowed operations:
push = list.append(x)
pop = list.pop()
peek = list[-1]
isEmpty = not list / or (len(list)==0)

Amortized time for
'''

def sort_stack(s):
    m, sidx, midx = [],0,0
    while sidx < len(s) or midx<len(m):
        sidx = max_search(s,m,sidx,midx)
        midx = min_search(s,m,sidx,midx)
    while len(m)>0: s.append(m.pop())
    return s

def max_search(s,m,sidx,midx):
    tmp = s.pop()
    while len(s)>sidx:
        if tmp < s[-1]: m.append(tmp); tmp = s.pop()
        else: m.append(s.pop())
    s.append(tmp)
    return sidx+1

def min_search(s,m,sidx,midx):
    tmp = m.pop()
    while len(m)>midx:
        if tmp > m[-1]: s.append(tmp);tmp=m.pop()
        else: s.append(m.pop())
    m.append(tmp)
    return midx+1

assert sort_stack([1,11,4,7,3,5]) == [11, 7, 5, 4, 3, 1]