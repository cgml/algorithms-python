#!/usr/bin/env python3
"""Run and time an optimal TSP solution."""

import math
import sys
import timeit
import itertools

def cost(route):
    sum = 0
    route.append(route[0])
    while len(route) > 1:
        p0, *route = route
        sum += math.sqrt((int(p0[0]) - int(route[0][0]))**2 + (int(p0[1]) - int(route[0][1]))**2)
    return sum

def tsp_bruteforce(data):
    d = float("inf")
    pmin = None
    for p in itertools.permutations(data):
        c = cost(list(p))
        if c <= d: d, pmin = c, p
    return pmin, d

def loaddata():
    data = """  70 162
                184 212
                259 157
                384 2
                191 50
                29 289
                381 109
                449 494
                438 403
                344 326"""
    return [[int(k) for k in p.split()] for p in data.strip().splitlines()]

pmin, d = tsp_bruteforce(loaddata())

print("Optimal route:", pmin)
print("Length:", d)

