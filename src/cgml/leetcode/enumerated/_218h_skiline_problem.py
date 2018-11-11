import heapq


class B:
    def __init__(self, h):
        self.h = h

    def __repr__(self):
        return str(self.h)


class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        q, horizon, out = [], [], []
        for idx, v in enumerate(buildings):
            x1, x2, h = v
            b = B(h)
            heapq.heappush(q, (x1, idx, b, 's'))
            heapq.heappush(q, (x2, idx, b, 'e'))

        cnt = 0
        while q:
            x, _, b, op = heapq.heappop(q)
            if op == 's':
                if not horizon or horizon[0][2].h < b.h: out.append([x, b.h])
                heapq.heappush(horizon, (-b.h, cnt, b))
                cnt += 1
            else:
                h = b.h
                b.h = None
                while horizon and not horizon[0][2].h: heapq.heappop(horizon)
                if not horizon or h > horizon[0][2].h:
                    out.append([x, 0 if not horizon else horizon[0][2].h])
        idx = 1
        while idx < len(out):
            if out[idx - 1][0] == out[idx][0]:
                out[idx - 1][1] = max(out[idx - 1][1], out[idx][1])
                out.pop(idx)
                idx = min(idx-1,1)
            elif out[idx - 1][1] == out[idx][1]:
                out.pop(idx)
                idx = min(idx - 1, 1)
            else:
                idx += 1
        return out


print(Solution().getSkyline([[2,4,7],[2,4,5],[2,4,6]]))
print(Solution().getSkyline([[0,2,3],[2,5,3]]))

print(Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
print([[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]])

class Solution2:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [(0,0)]
        corner = sorted({b[0] for b in buildings}|{b[1] for b in buildings})
        heap = [(0,float('inf'))]
        heapq.heapify(heap)
        n = len(buildings)
        j = 0
        for x in corner:
            while j<n and buildings[j][0]==x:
                heapq.heappush(heap,(-buildings[j][2],buildings[j][1]))
                j += 1
            while heap[0][1]<=x:
                heapq.heappop(heap)
            if res[-1][1]!=-heap[0][0]:
                res.append((x,-heap[0][0]))
        return res[1:]
