#
# Complete the 'wordBreakCount' function below.
#
# The function accepts STRING_ARRAY dictionary as parameter
# and the original STRING txt on which segmentation is to be
# performed.
# The function returns the count of all possible segmentation
#
def wordBreakCount(dictionary, txt):
    # Write your code here
    word_set = set()
    word_len = set()
    for word in dictionary:
        word_set.add(word)
        word_len.add(len(word))

    n = len(txt)
    wbc = [0 for i in range(n + 1)]

    for idx in range(1, (n + 1)):

        if txt[0:idx] in word_set:
            wbc[idx] += 1

        for l in word_len:
            if idx - l >= 0:

                if idx - l >= 0 and txt[idx - l:idx] in word_set:
                    wbc[idx] += wbc[idx - l]
    return wbc[n] % 1000000007