'''

Time Complexity: O(max(N,M))
Space Complexity: O(max(N,M)+1)

Options:
- with accumulator (potential issue overflow, easier addition)
- without accumulator (more complex addition)


It can be rewritten to replace int(string) => ord(char) - ord(0 char) to get more 'native solution'
ord: char=> int
chr: int=> char

'''

def add_binary(s1,s2):
    accum, idx1, idx2, result = 0, len(s1)-1, len(s2)-1, []
    while accum > 0 or idx1 >= 0 or idx2 >= 0:
        current_bit = 0
        if idx1 >= 0: current_bit, idx1 = int(s1[idx1]), idx1 - 1
        if idx2 >= 0: current_bit, idx2 = current_bit+int(s2[idx2]), idx2 - 1
        if accum > 0: current_bit, accum = current_bit + 1, accum - 1
        if current_bit > 1: current_bit, accum = current_bit - 2, accum + 1
        result.append(str(current_bit))
    return "".join(reversed(result))

assert add_binary("11","11") == "110"
assert add_binary("1","11") == "100"
assert add_binary("11","1") == "100"
