import random

def make_input(pattern, n, rng):
    if pattern == "random":
        return [rng.randrange(n * 10) for _ in range(n)]
    if pattern == "sorted":
        return list(range(n))
    if pattern == "reversed":
        return list(range(n, 0, -1))
    if pattern == "nearly":                 # about 2% of neighbours swapped
        a = list(range(n))
        for i in range(n - 1):
            if rng.random() < 0.02:
                a[i], a[i + 1] = a[i + 1], a[i]
        return a
    if pattern == "duplicates":             # only 10 distinct values
        return [rng.randrange(10) for _ in range(n)]
    raise ValueError(f"unknown pattern: {pattern}")