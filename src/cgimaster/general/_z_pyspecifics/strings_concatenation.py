'''
Efficient String Concatenation in Python

- String objects are immutable

- Profiling shown that naive string concatenation is comparable with method of list comprehension join
- Also there is intelligent internal optimization for range naive range joins, which result into only one call
'''

import cProfile
import tracemalloc
import random

class memory_profiler(object):
    def __init__(self, f):
        self.f = f

    def __call__(self,N):
        print("Start memory profiling for: ", self.f.__name__)
        tracemalloc.start()
        self.print_stats(tracemalloc.take_snapshot())
        self.f(N)
        self.print_stats(tracemalloc.take_snapshot())
        print("...completed memory profiling [", self.f.__name__, "]")
        tracemalloc.stop()

    def print_stats(self,snapshot):
        top_stats = snapshot.statistics('lineno')
        print("[ Top 10 ]")
        for stat in top_stats[:10]: print(stat)


#Runtime(range to 1M) = 4 function calls in 19.182 seconds
#Runtime(random for 100K) = 10000004 function calls in 6.795 seconds
def string_concat_naive(N):
    out_str = ''
    for c in range(N): out_str += str(random.random())
    return out_str
#Runtime = 100000005 function calls in 30.988 seconds
def string_with_list(N):
    str_list = []*N
    for c in range(N): str_list.append(str(random.random()))
    return ''.join(str_list)

#Runtime = 6 function calls in 20.442 seconds
def string_with_comprehensions(N):
    return ''.join([str(random.random()) for c in range(N)])

#Runtime = 100000007 function calls in 30.799 seconds
def string_with_inmemory_file(N):
    from io import StringIO
    file_str = StringIO()
    for c in range(N): file_str.write(str(random.random()))
    return file_str.getvalue()

print('Naive:')
cProfile.run("string_concat_naive(10000000)")

print('List:')
cProfile.run("string_with_list(10000000)")

print('Comprehensions:')
cProfile.run("string_with_comprehensions(10000000)")

print('InMem File:')
cProfile.run("string_with_inmemory_file(10000000)")


# string_concat_naive(10000000)
# string_with_comprehensions(10000000)