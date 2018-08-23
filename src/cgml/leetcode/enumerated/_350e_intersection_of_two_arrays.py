class Solution:
    def intersect(self, nums1, nums2):
        d, result = {}, []
        for item in nums1: d[item] = d.get(item, 0) + 1
        for item in nums2:
            counter = d.get(item, 0)
            if counter > 0:
                result.append(item)
                if counter == 1:
                    del d[item]
                else:
                    d[item] = counter - 1
        return result

