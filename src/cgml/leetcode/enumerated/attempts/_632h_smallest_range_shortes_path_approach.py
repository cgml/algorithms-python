import heapq
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

class DynamicUpdate():
    #Suppose we know the x range
    min_x = -100
    max_x = 100

    def on_launch(self):
        #Set up plot
        self.figure, self.ax = plt.subplots()
        self.points, = self.ax.plot([], [], 'o')
        self.points_visited, = self.ax.plot([], [])
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        self.ax.set_xlim(self.min_x, self.max_x)
        #Other stuff
        self.ax.grid()
        #...

    def set_points(self, xdata, ydata):
        #Update data (with the new _and_ the old points)
        self.points.set_xdata(xdata)
        self.points.set_ydata(ydata)
        #Need both of these in order to rescale
        self.redraw()

    def set_points_visited(self, xdata, ydata):
        #Update data (with the new _and_ the old points)
        self.points_visited.set_xdata(xdata)
        self.points_visited.set_ydata(ydata)
        self.redraw()
    def redraw(self):
        #Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        #We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

d = DynamicUpdate()
d.on_launch()

class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if len(nums) == 1: return [nums[0][0], nums[0][ 0]]
        paths = []
        for idx in range(len(nums[0])):
            length, minpath, maxpath = self._find_shortest_path(idx, nums)
            if length is None:
                print("ERROR. Solution not found for {}, {}".format(idx, nums))
            else:
                paths.append((length, minpath, maxpath))
        paths = sorted(paths)
        return [self._fixback(paths[0][1]), self._fixback(paths[0][2])]

    def _fix(self, x): return x + 10**5
    def _fixback(self, x): return x - 10**5

    def _find_shortest_path(self, idx, nums):
        xdata, ydata = [], []
        for lidx, num in enumerate(nums):
            for n in num:
                xdata.append(n)
                ydata.append(lidx)
        d.set_points(xdata,ydata)
        d.redraw()
        xdata_visited, ydata_visited = [],[]
        q = [(0, 0, idx, self._fix(nums[0][idx]), self._fix(nums[0][idx]), [(0,idx,idx)])]
        # length of the path, list idx, item idx in a list, do not include [] -path store just range
        visited = set()
        while q:
            length, lidx, iidx, minpath, maxpath, path = heapq.heappop(q)  #
            xdata_visited.append(nums[lidx][iidx])
            ydata_visited.append(lidx)
            #d.set_points_visited(xdata_visited, ydata_visited)
            d.set_points_visited([nums[y][x] for w,y,x in path], [y for w,y,x in path])

            if (lidx, iidx) in visited: continue
            if lidx == len(nums) - 1:
                return (length, minpath, maxpath)
            visited.add((lidx, iidx))
            # curval = 10**5 + nums[lidx][iidx]
            for nidx in range(len(nums[lidx + 1])):
                newmin = min(minpath, self._fix(nums[lidx + 1][nidx]))
                newmax = max(maxpath, self._fix(nums[lidx + 1][nidx]))
                newlength = newmax - newmin
                heapq.heappush(q, (newlength, lidx + 1, nidx, newmin, newmax, path+[(newlength,lidx+1,nidx)]))  #
        return None, None, None

# nums = [[-51,-9,-3,1,1,7,10,11],
nums = [[11],
        [17,26,32,32,33,37],
        [5,45,88,90,91],
        [23,35,64,71,95,95,95,96],
        [-25,-15,-12,41],
        [20,30,31,32,40],
        [9,13],
        [-11,34,36,43,45,46],
        [86,97,99,100],
        [-4,37,38],
        [-2,72,74,76,80,90,91],
        [-14,12,26,32,32,32,33,33,35],
        [58,65,88,99],
        [-30,0,23,23,25,25,25,26],
        [-53,-26,-19,-4,18,41],
        [-7,13,15],[15,17,17,18],
        [56,58,62],
        [-17,-14,8,11,16,18,18,19,19,19,20],
        [6,58,70,74,74,75,75,75,75,76]]
# for num in nums:
#     for idx in range(len(num)):
#         num[idx]+=1000
print('Actual:   ', Solution().smallestRange(nums))
print('Expected: [11,86]')