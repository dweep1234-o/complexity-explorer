import random
from inputs import make_input
from algorithms import linear_search, binary_search

for p in ["random", "sorted", "reversed", "nearly", "duplicates"]:
    a = make_input(p, 1000, random.Random(1))
    print(f"{p:11} length={len(a)} first={a[:5]}")

s = sorted(make_input("random", 1000, random.Random(1)))
targets = [x + 0.5 for x in range(0, 200, 5)]   # absent values
_, lin = linear_search(s, targets)
_, bin_ = binary_search(s, targets)
print("linear ops/query:", lin)      # should be exactly 1000
print("binary ops/query:", bin_)     # should be about 10