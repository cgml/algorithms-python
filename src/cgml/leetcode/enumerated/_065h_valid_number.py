import re

class Solution:
    def isNumber(self, s):
        return re.match(r'^\s*(?:[+-]?)(([0-9]+\.?[0-9]*){1,1}|(\.[0-9]+){1,1})(?:(e([\+-]?[0-9]+))?)\s*$',s.lower()) is not None

class SolutionDFA(object):
  def isNumber(self, s):
      """
      :type s: str
      :rtype: bool
      """
      #define a DFA
      state = [{},
              {'blank': 1, 'sign': 2, 'digit':3, '.':4},
              {'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
              {'blank':9}]
      currentState = 1
      for c in s:
          if c >= '0' and c <= '9':
              c = 'digit'
          if c == ' ':
              c = 'blank'
          if c in ['+', '-']:
              c = 'sign'
          if c not in state[currentState].keys():
              return False
          currentState = state[currentState][c]
      if currentState not in [3,5,8,9]:
          return False
      return True

assert SolutionDFA().isNumber("2e10")