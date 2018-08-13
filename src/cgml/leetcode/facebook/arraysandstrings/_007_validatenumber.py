import re

class SolutionRE:
    def isNumber(self, s):
        return re.match(r'^\s*(?:[+-]?)(([0-9]+\.?[0-9]*){1,1}|(\.[0-9]+){1,1})(?:(e([\+-]?[0-9]+))?)\s*$',s.lower()) is not None

class SolutionCocky:
    def isNumber(self, s):
        try: float(s.strip())
        except Exception: return False




assert not SolutionRE().isNumber("0e ")
assert not SolutionRE().isNumber("1 4")
assert not SolutionRE().isNumber(".44.4")
assert SolutionRE().isNumber(".1")
assert not SolutionRE().isNumber(" ")
assert SolutionRE().isNumber("0")
assert not SolutionRE().isNumber(".")
assert SolutionRE().isNumber("123")
assert not SolutionRE().isNumber("123 32")
assert SolutionRE().isNumber("123.12")
assert not SolutionRE().isNumber("1 2 3. 1 2e 1 0")
assert not SolutionRE().isNumber("123.12e")
assert not SolutionRE().isNumber("123.12e")
assert SolutionCocky().isNumber("0")
assert SolutionCocky().isNumber("2e10")