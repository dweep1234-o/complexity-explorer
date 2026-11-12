import random
import time
import numpy as np
from inputs import make_input


def sizes_between(lo=100, hi=8000, points=9):
    """Log-spaced input sizes, e.g. 100, 178, 316, ..."""
    return sorted({int(round(x)) for x in np.geomspace(lo, hi, points)})


def benchmark(algo, pattern, sizes, trials=3):
    """Return (mean ops, mean milliseconds) for each size."""
    ops_mean, ms_mean = [], []
    for n in sizes:
        ops_trials, ms_trials = [], []
        for t in range(trials):
            rng = random.Random(7919 * t + n)     # same inputs for every algorithm
            base = make_input(pattern, n, rng)
            t0 = time.perf_counter()
            _, ops = algo(base)
            ms_trials.append((time.perf_counter() - t0) * 1000)
            ops_trials.append(ops)
        ops_mean.append(float(np.mean(ops_trials)))
        ms_mean.append(float(np.mean(ms_trials)))
    return np.array(ops_mean), np.array(ms_mean)


def fitted_slope(sizes, ops):
    """Least-squares slope on a log-log plot: the empirical exponent."""
    k, _ = np.polyfit(np.log2(sizes), np.log2(ops), 1)
    return float(k)


def fitted_constant(sizes, ops, f):
    """Geometric mean of ops / f(n): the constant hidden by Big-O."""
    sizes = np.asarray(sizes, dtype=float)
    return float(np.exp(np.mean(np.log(ops) - np.log(f(sizes)))))

def search_benchmark(search, pattern, sizes, trials=3, queries=200):
    """Like benchmark(), but for searches: sort the data, then query absent targets."""
    ops_mean = []
    for n in sizes:
        vals = []
        for t in range(trials):
            rng = random.Random(7919 * t + n)
            base = sorted(make_input(pattern, n, rng))
            mx = max(base) if base else 1
            targets = [rng.randrange(mx + 1) + 0.5 for _ in range(queries)]
            _, ops = search(base, targets)
            vals.append(ops)
        ops_mean.append(float(np.mean(vals)))
    return np.array(ops_mean)