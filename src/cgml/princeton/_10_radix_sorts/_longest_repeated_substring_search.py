'''
Important applications:
- substring search in large documents
- longest repeated substring
    (e.g. genomics data, crypto-analysis, data compression, repetitions in music)

Brute force:
- For each pair i & j do matching. TC: O(DN^2) where D is max length of substring

Efficient:
- Build suffixes: Linear Time
- Sort suffixes (will bring similar strings together): Linear Time with Radix sort
- Find similar strings: O(DN)

Space Complexity: O(N^2)
'''

def longest_common_prefix(s1,s2):
    result = 0
    while result<min(len(s1),len(s2)) and s1[result] == s2[result]: result+=1
    return result

def lrs(text):
    N = len(text)
    suffixes = [""]*N

    # Java substring - linear time and space, python
    for i in range(N): suffixes[i] = text[i:]

    # O(nlogn). Can be done in O(DN) with 3 way string quick sort (only if D is not large)
    # Manber-Mayers (NlogN) and Suffix tries (N) are even better can solve in linearithmic and linear time
    suffixes.sort()

    result = ""
    for i in range(N-1):
        lcp1 = longest_common_prefix(suffixes[i],suffixes[i+1])
        if lcp1 > len(result): result = suffixes[i][:lcp1]
    return result

text =  """ Space Efficiency
Suffix arrays were introduced by Manber & Myers (1990) in order to improve over the space requirements of suffix trees: Suffix arrays store {\displaystyle n} n integers. Assuming an integer requires {\displaystyle 4} 4 bytes, a suffix array requires {\displaystyle 4n} 4n bytes in total. This is significantly less than the {\displaystyle 20n} 20n bytes which are required by a careful suffix tree implementation.[6]

However, in certain applications, the space requirements of suffix arrays may still be prohibitive. Analyzed in bits, a suffix array requires pace, whereas the original text over an alphabet of size {\displaystyle \sigma } \sigma  only requires {\displaystyle {\mathcal {O}}(n\log \sigma )} {\mathcal  {O}}(n\log \sigma ) bits. For a human genome with {\displaystyle \sigma =4} \sigma =4 and {\displaystyle n=3.4\times 10^{9}} n=3.4\times 10^{9} the suffix array would therefore occupy about 16 times more memory than the genome itself.

Such discrepancies motivated a trend towards compressed suffix arrays and BWT-based compressed full-text indices such as the FM-index. These data structures require only space within the size of the text or even less.

Construction Algorithms
A suffix tree can be built in  and can be converted into a suffix array by traversing the tree depth-first also in , so there exist algorithms that can build a suffix array in .

A naive approach to construct a suffix array is to use a comparison-based sorting algorithm. These algorithms require uffix comparisons, but a suffix comparison runs in  time, so the overall runtime of this approach is {\displaystyle {\mathcal {O}}(n^{2}\log n)} {\mathcal  {O}}(n^{2}\log n).

More advanced algorithms take advantage of the fact that the suffixes to be sorted are not arbitrary strings but related to each other. These algorithms strive to achieve the following goals:[7]

minimal asymptotic complexity {\displaystyle \Theta (n)} \Theta (n)
lightweight in space, meaning little or no working memory beside the text and the suffix array itself is needed
fast in practice
One of the first algorithms to achieve all goals is the SA-IS algorithm of Nong, Zhang & Chan (2009). The algorithm is also rather simple (< 100 LOC) and can be enhanced to simultaneously construct the LCP array.[8] The SA-IS algorithm is one of the fastest known suffix array construction algorithms. A careful implementation by Yuta Mori outperforms most other linear or super-linear construction approaches.

Beside time and space requirements, suffix array construction algorithms are also differentiated by their supported alphabet: constant alphabets where the alphabet size is bound by a constant, integer alphabets where characters are integers in a range depending on {\displaystyle n} n and general alphabets where only character comparisons are allowed.[9]

Most suffix array construction algorithms are based on one of the following approaches:[7]

Prefix doubling algorithms are based on a strategy of Karp, Miller & Rosenberg (1972). The idea is to find prefixes that honor the lexicographic ordering of suffixes. The assessed prefix length doubles in each iteration of the algorithm until a prefix is unique and provides the rank of the associated suffix.
Recursive algorithms follow the approach of the suffix tree construction algorithm by Farach (1997) to recursively sort a subset of suffixes. This subset is then used to infer a suffix array of the remaining suffixes. Both of these suffix arrays are then merged to compute the final suffix array.
Induced copying algorithms are similar to recursive algorithms in the sense that they use an already sorted subset to induce a fast sort of the remaining suffixes. The difference is that these algorithms favor iteration over recursion to sort the selected suffix subset. A survey of this diverse group of algorithms has been put together by Puglisi, Smyth & Turpin (2007).
A well-known recursive algorithm for integer alphabets is the DC3 / skew algorithm of Kärkkäinen & Sanders (2003). It runs in linear time and has successfully been used as the basis for parallel[10] and external memory[11] suffix array construction algorithms.

Recent work by Salson et al. (2009) proposes an algorithm for updating the suffix array of a text that has been edited instead of rebuilding a new suffix array from scratch. Even if the theoretical worst-case time complexity is {\displaystyle {\mathcal {O}}(n\log n)} {\mathcal {O}}(n\log n), it appears to perform well in practice: experimental results from the authors showed that their implementation of dynamic suffix arrays is generally more efficient than rebuilding when considering the insertion of a reasonable number of letters in the original text.
"""

print(lrs(text))