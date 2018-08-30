'''
Problem: 2D orthogonal range search

API:
    insert 2d key
    delete 2d key
    search for 2d key
    range search: find all keys in 2d range
    range count: number of all keys in 2d range

Implementations:

Grid
    - Time Complexity: O(1+N/M^2)
    - Space Complexity: O(M^2+N)
    - rule of thumb M~ sqrt(N)
    - Performs poorly due to clustering phenomena

Space partitioning trees (recursive subdivision of multi-dimensional space)
    Idea:
        insert:
            recursively partition plane into two half-planes
            iterate between odd (horizontal) and even (vertical) levels

        range search:
            check if point is in rectangle
            recursively search left/bottom - if any could fall in rectangle
            recursively search right/top - if any could fall in rectangle

            Time Complexity:
                Typical Case (small rectangle) - O(R+logN)
                Worst Case (if tree is balanced) - O(R+sqrtN)

        find closest point (nearest neighbor search):
            check distance from current point
            recursively search left/bottom - if it could contain closer point
            recursively search right/top - if it could contain closer point

            Time Complexity:
                In practice O(logN)
                Worst case O(N)

    Examples in nature:
        - Flocking birds:
            Collision avoidance - point away from k nearest birds
            Flock centering - point towards center of mass of k nearest birds
            Velocity Matching - update velocity to k nearest birds

KD tree:
    Idea: Recursively partition one dimension at a time
    Discovered by Jon Bentley

Problem: N-body simulation in physics
    Goal: simulate the motion of N particles, mutually affected by gravity
    Brute-force: F = G*m1*m2/r^2

    Solution idea:
        if particle is far away from cluster of particles,
        treat cluster of particles as single aggregate particle
        compute forces between particles and center mass of aggregate

        Solution uses 3d trees, Time Complexity -> O(NlogN) not O(N^2)

        Discovered by Appel,

'''

