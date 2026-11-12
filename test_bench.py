from algorithms import bubble_sort, merge_sort
from bench import sizes_between, benchmark, fitted_slope

sizes = sizes_between(100, 2000, points=6)
print("sizes:", sizes)

ops, ms = benchmark(bubble_sort, "random", sizes, trials=2)
print("bubble ops:", ops.round(0))
print("bubble slope:", round(fitted_slope(sizes, ops), 2))

ops, ms = benchmark(merge_sort, "random", sizes, trials=2)
print("merge slope:", round(fitted_slope(sizes, ops), 2))