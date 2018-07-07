import math
def swap_number(num):
    k = num
    N=int(math.log10(num))
    for i in range(int(N/2)+1):
        k = k - e_n(num, N - i) * 10 ** (N - i) + e_n(num, N - i) * 10 ** i - e_n(num,i)*10**i + e_n(num,i)*10**(N-i)
    return k

def e_n(num,position):
    return int((num%(10**(position+1)) - num%(10**position))/(10**position))


assert swap_number(123456) == 654321
assert swap_number(123456788) == 887654321