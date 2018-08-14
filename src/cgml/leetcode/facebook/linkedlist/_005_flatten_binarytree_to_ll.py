from cgml.leetcode.facebook.linkedlist.utils import *

class Solution(object):
    def helper(self,parent,left):
        pass

    def flatten(self, root):
        pass
'''     
    1
   / \
  2   9
 / \   \
3   7   10
   / \
  5   8
  
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          7
           \
            8
             \
              9
               \
                10

'''
print(serializeBT(Solution().flatten(deserializeBT("1,2,3,#,4,#,#,5,#,6,#,#"))))
assert serializeBT(Solution().flatten(deserializeBT("1,2,3,#,4,#,#,5,#,6,#,#")))== "1,#,2,#,3,#,4,#,5,#,6,#,#"