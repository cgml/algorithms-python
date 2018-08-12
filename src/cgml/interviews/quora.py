# # [1 3 7 8 11 8 7] -> 11
# # [1 3 7 8 11] -> 11
# # [11 8 7] -> 11

# # [11] -> 11
# # [] -> None


# # invalid:
# # [1 3 3 7 4]



# '''

# [1 3 7 8 11 8 7]

# 7 / 8 < 1 =>
# right_idx

# 11 / 8 => left_idx
#     O(log N)
#     O(1)
# '''



# def find_max(a, right_idx = 0, left_idx = None):
#     if not left_idx: left_idx = len(a) - 1
#     a_len = left_idx - right_idx + 1
#     if a_len == 1: return a[right_idx]
#     if a_len == 2: return max(a[right_idx], a[right_idx +1])
#     mid_idx = right_idx + int(a_len / 2)
#     if a[mid_idx-1]/a[mid_idx] < 1: return find_max(a, mid_idx, left_idx)
#     else: return find_max(a, right_idx, mid_idx-1)

# assert find_max([11]) == 11
# assert find_max([11,10]) == 11
# assert find_max([10,11]) == 11
# assert find_max([10,11,1]) == 11
# assert find_max([1, 3, 11, 8, 7]) == 11
# assert find_max([1, 3, 7, 8, 11, 8, 7]) == 11
# assert find_max([1, 3, 7, 8, 11]) == 11
# assert find_max([1, 3, 7, 8, 11, 12, 31, 3, 1]) == 31
# print (find_max([1,3, 7, 8, 11, 8, 7]))

# assert find_max([k for k in range(1000001)]) == 1000000



'''

a = [1 1 3 3 2 2 2 2 2 4 5 7] -> 10
n = len(a)
1 <= a[i] <= n

b subset of a
if x in b, then  not x+1 and not x-1 not in b
valid:
b = [1 3 1]
b = [2 2 2 2 2]
b = [1 1 3 3]
not valid:
b = [2 3]
b = [1 2 2 2]


-------------------

SC - O(N) => O(1)
TC - O(N)

b_counts = [2, 10, 6, 4, 10 , 5, 0, 0]
total_sum = sum(b_counts)
b_total_sums = max([total_sum - 10, total_sum - 8, total_sum - 10])

'''
