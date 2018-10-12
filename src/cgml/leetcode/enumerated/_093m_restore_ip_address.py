class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result, mem = set(), {}
        self._helper(s, result, [], mem)
        return list(result)

    def _helper(self, s, result, address, mem):
        if mem.get('.'.join(address), False): return
        mem['.'.join(address)] = True

        if not s and len(address) == 4: result.add('.'.join(address))
        if len(address) >= 4: return

        def check(spart, idx):
            if len(spart) < idx or idx > 1 and spart[0] == '0': return False
            part = int(spart[:idx])
            return part >= 0 and part <= 255

        for idx in range(1, 4):
            if check(s, idx):
                self._helper(s[idx:], result, address + [s[:idx]], mem)
