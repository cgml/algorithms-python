class Solution(object):
    def helper(self, str, s, e):
        while s<e and e<len(str): str[s],str[e],s,e=str[e],str[s],s+1,e-1

    def reverseWords(self, str):
        self.helper(str,0,len(str)-1)
        s,e=0,0
        while s<len(str):
            while e<len(str) and str[e] != " ": e+=1
            while s<len(str) and str[s] == " ": s+=1
            self.helper(str,s,e-1)
            s,e=e,e+1

class SolutionExtraSpace(object):
    def reverseWords(self, str):
        if str:
            result = list(" ".join([word for word in ''.join(str).split(" ")][::-1]))
            for idx in range(len(str)): str[idx]=result[idx]

input = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Solution().reverseWords(input)
print(input)
assert input == ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

