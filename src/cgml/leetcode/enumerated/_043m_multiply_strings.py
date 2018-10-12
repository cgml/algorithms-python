class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or num1 == '0' or num2 == '0' or not num2: return '0'
        d, result, lidx = {}, '0', 0
        for c in set(num1):  d[c] = self._multiply(num2, int(c)) if c != '0' else '0'
        for idx, c in enumerate(reversed(num1)):
            result = self._sum(result, d[c] + (''.join(['0'] * idx) if idx > 0 else ''))
        while result[lidx] == '0': lidx += 1
        return result[lidx:]

    def _multiply(self, num, n):
        acc, result = 0, ''
        while num:
            nv = acc + int(num[-1]) * n
            result, acc, num = str(nv % 10) + result, nv // 10, num[:-1]
        return str(acc) + result if acc else result

    def _sum(self, num1, num2):
        acc, result = 0, ''
        while num1 or num2 or acc > 0:
            nv = acc
            if num1: nv += int(num1[-1])
            if num2: nv += int(num2[-1])
            result, acc, num1, num2 = str(nv % 10) + result, nv // 10, num1[:-1], num2[:-1]
        return result

class SolutionT:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product=[0]*(len(num1)+len(num2))
        pos=len(product)-1
        for n1 in reversed(num1):
            tmp=pos
            for n2 in reversed(num2):
                product[tmp]+=int(n1)*int(n2)
                product[tmp-1]+=product[tmp]//10
                product[tmp]%=10
                tmp-=1
            pos-=1
        p=0
        while p<len(product)-1 and product[p]==0:
            p+=1
        return ''.join(map(str,product[p:]))

class SolutionCheat:
    def multiply(self, num1, num2):
        return str(int(num1) * int(num2))

print(Solution().multiply('7234333333333333334444444444444455555555444449827409187304918723041827401298734012873412984',
                          '327412937412984712874012834728937491287410293847'))
print(SolutionT().multiply('7234333333333333334444444444444455555555444449827409187304918723041827401298734012873412984',
                           '327412937412984712874012834728937491287410293847'))
print(SolutionCheat().multiply('7234333333333333334444444444444455555555444449827409187304918723041827401298734012873412984',
                           '327412937412984712874012834728937491287410293847'))