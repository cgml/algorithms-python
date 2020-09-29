from collections import deque


def zombieCluster(zombies):
    n = len(zombies)
    visited = [0] * n
    res = 0

    def zombiesBFS(z):
        q = deque([z])
        while q:
            z = q.popleft()
            for i in range(n):
                if not visited[i] and zombies[z][i] == '1':
                    visited[i] = 1
                    q.append(i)

    for z in range(n):
        if not visited[z]:
            res += 1
            visited[z] = 1
            zombiesBFS(z)

    return res