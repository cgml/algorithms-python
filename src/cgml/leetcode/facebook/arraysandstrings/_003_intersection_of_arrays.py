def intersect(nums1,nums2):
    d, result = {}, []

    for item in nums1: d[item]=d.get(item,0)+1
    for item in nums2:
        counter = d.get(item, 0)
        if counter > 0:
            result.append(item)
            if counter == 1: del d[item]
            else: d[item] = counter - 1
    return result


def intersect_sorted(nums1,nums2):
    idx1, idx2, result = 0, 0, []
    while idx1 < len(nums1) and idx2 < len(nums2):
        while idx1 < len(nums1) and nums1[idx1] < nums2[idx2]: idx1 += 1
        while idx2 < len(nums2) and idx1 < len(nums1) and nums2[idx2] < nums1[idx1]: idx2 += 1
        if idx1 < len(nums1) and idx2 < len(nums2) and nums1[idx1] == nums2[idx2]:
            result.append(nums1[idx1])
            idx1, idx2 = idx1+1, idx2+1
    return result


assert sorted(intersect([4,9,5], [9,4,9,8,4])) == sorted([4,9])
assert sorted(intersect_sorted(sorted([4,9,5]), sorted([9,4,9,8,4]))) == sorted([4,9])
assert sorted(intersect_sorted([1,1], [1,2])) == sorted([1])