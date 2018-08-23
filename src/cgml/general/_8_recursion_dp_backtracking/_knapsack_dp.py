'''
Knapsack - capacity
Items: Value, Cost (e.g. $, kg)

Versions:
    - fractional (w/o repetitions) - can be solved by greedy algorithm
    - discrete
        - with repetition
        - without repetition

Example:
    W: 10
    Items: 6kg/$30, 3/$14, 4/$16, 2/$9

    - discrete w/o repetitions: $46
    - discrete w/ repetitions: $48
    - fractional (w/o repetitions) = $48.5

'''
import numpy as np

def knapsack_norep(W,values,weights):
    N = len(values)
    mem = np.zeros((W+1,N+1),dtype=np.int32)
    for i in range(1,N+1):
        for w in range(1,W+1):
            mem[w,i]=mem[w,i-1]
            if weights[i-1] <= w: mem[w, i] = max(mem[w-weights[i-1], i-1]+values[i-1], mem[w,i])
    return mem[-1][-1]

assert knapsack_norep(10,[30,14,16,9],[6,3,4,2]) == 46
assert knapsack_norep(50,[60, 100, 120],[10, 20, 30]) == 220