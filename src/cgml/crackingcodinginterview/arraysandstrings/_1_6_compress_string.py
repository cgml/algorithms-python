def string_compress(s):
    idx, result, curc = 0,[],""
    for i, c in enumerate(s):
        if c!=curc:
            if i - idx > 0: result += "{}{}".format(curc,i-idx)
            curc=c
            idx=i
    compressed = "".join(result + ["{}{}".format(curc,len(s)-idx)])
    return compressed if len(compressed) < len(s) else s

assert string_compress("aabcccccaa")=="a2b1c5a2"
assert string_compress("abc")=="abc"
