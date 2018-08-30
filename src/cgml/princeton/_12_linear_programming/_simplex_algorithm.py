'''
Developed by George Dantzig at 1947
Ranked as one of the top 10 scientific algorithms of 20th century

Goal: Optimize resources allocation (e.g. solve Brewer's problem)

Idea:
    - Start at extreme point
    - Pivot from one extreme point to adjacent one (never decreasing adjacent function)
    - Repeat until optimal

Solve by linear algebra operations

Basis - subset of m in n variables
Basic Feasible Solution (BFS)
    - Set n-m nonbasic variables to 0, solve remaining m variables
    - Solve m equations and m unknowns
    - If unique and feasible => BFS
    - BFS <=> extreme point

C - corn
H - h.
M - m.
maximize                Z

subj. to constraints    13A     +   23B                         -Z      = 0
                        5A      +   15B     + Sc                        = 480
                        4A      +   4B              + Sh                = 160
                        35A     +   20B                     +Sm         = 1190

                        A       ,   B   ,   Sc   ,    Sh ,  Sm          >= 0

'''

from scipy.optimize import linprog

c = [-1, 4]
A = [[-3, 1], [1, 2]]
b = [6, 4]
x0_bnds = (None, None)
x1_bnds = (-3, None)
res = linprog(c, A, b, bounds=(x0_bnds, x1_bnds))
print(res)