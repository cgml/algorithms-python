'''
Extension of ordered symbol table:
    - insert k-v pair
    - search for key k
    - delete key k
    - range search: search for all keys between k1 and k2
    - range count: number of keys between k1 and k2

Application:
    database queries


Geometric interpretation:
    keys are points on a line
    find/count points in a given 1d interval


Implementations:
    - Unordered array
        insert          - O(1)
        range count     - O(N)
        range search    - O(N)
    - Unordered array
        insert          - O(N)
        range count     - O(logN)
        range search    - O(R+logN)
    - BST
        insert          - O(logN)
        range count     - O(logN)
        range search    - O(R+logN)

'''