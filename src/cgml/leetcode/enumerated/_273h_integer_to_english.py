'''
273. Integer to English Words (Arrays  & Strings: Hard)
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:
```
Input: 123
Output: "One Hundred Twenty Three"
```
Example 2:
```
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
```
Example 3:
```
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```
Example 4:
```
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
```
'''

class Solution:
    def helper(self, num, words):
        result = []
        if num>=10**9: result+=self.helper(num//10**9, words)+["Billion"]+self.helper(num % 10**9, words)
        elif num>=10**6: result+=self.helper(num//10**6, words)+["Million"]+self.helper(num % 10**6, words)
        elif num >= 10**3: result += self.helper(num//10**3, words)+["Thousand"]+self.helper(num%10**3, words)
        elif num >= 10 ** 2: result += self.helper(num // 10 ** 2, words)+["Hundred"]+self.helper(num % 10 ** 2, words)
        elif num >= 20: result += [words[(num-20)//10+20], words[num%10]]
        else: result+=[words[num]]
        return result

    def numberToWords(self, num):
        if num == 0: return "Zero"
        words = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        return " ".join([w for w in self.helper(num, words) if len(w) > 0])


class SolutionV2:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "Zero"
        words = {
            1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine",
            10:"Ten",
            11:"Eleven",
            12:"Twelve",
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"Nineteen",
            20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety",
            100:"Hundred",
            1000:"Thousand",
            10**6:"Million",
            10**9:"Billion",
            10**12: "Trillion"
        }
        idx = 0
        result = [[]]
        num = list(str(num))[::-1]

        def convert_dozens(num, words):
            n = int("".join(num[::-1]))
            if n > 10 and words.get(n): return [words.get(n)]
            elif n > 10: return [words.get(int(n/10)*10), words.get(n%10)]
            else:
                if words.get(n): return [words.get(n)]
                else: return []

        def convert_hundreds(num,words):
            n = int("".join(num[::-1]))
            if n >= 100: return [words.get(n // 100),words.get(100)]+convert_dozens(num[:-1],words)
            else: return convert_dozens(num[:-1],words)

        curpower = 0
        while idx < len(num):
            if curpower > 0: result = [[words.get(10**(curpower*3))]]+result
            if idx+2<len(num): result[0] = convert_hundreds(num[idx:idx+3], words)+result[0]
            else: result[0] = convert_dozens(num[idx:],words)+result[0]
            idx+=3
            curpower+=1
        output = []
        for idx, r in enumerate(result):
            if len(result) > 1 and (len(r) > 1 or idx == len(result)-1): output += r
            elif len(result) == 1: output += r
        return " ".join(output)



assert Solution().numberToWords(0) == "Zero"
assert Solution().numberToWords(100000) == "One Hundred Thousand"
assert Solution().numberToWords(1000000) == "One Million"
assert Solution().numberToWords(1000000000) == "One Billion"
assert Solution().numberToWords(1000000001) == "One Billion One"
assert Solution().numberToWords(1005000000) == "One Billion Five Million"
assert Solution().numberToWords(100) == "One Hundred"
assert Solution().numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"
assert Solution().numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
assert Solution().numberToWords(1234567891) == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"