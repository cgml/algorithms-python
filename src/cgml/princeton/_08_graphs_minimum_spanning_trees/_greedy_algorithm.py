'''
Assumptions:
    Edge weights are distinct (If not still works)
    Graph is connected (If not - will get minimum spanning forest)
Definitions:
    Cut - partition of two sets into two non-empty sets
    Crossing edge - connects vertex from one set to another
Cut property:
    Given any cut - the crossing edge of minimum weight is in MST

Idea:
    Iteratively:
     1. take cuts which do not contain edges of MST,
     2. select minimal edge and add it to MST,
     3. repeat until MST has V-1 edge (where V is # of Vertices in G)
'''