from algorithms import bubble_sort, merge_sort
from bench import sizes_between, benchmark
from plot import plot_results

sizes = sizes_between(100, 2000, points=6)
results = {}
for name, algo in [("bubble", bubble_sort), ("merge", merge_sort)]:
    ops, _ = benchmark(algo, "random", sizes, trials=2)
    results[name] = ops

fig = plot_results(sizes, results, "random")
fig.savefig("test_plot.png", dpi=120)
print("saved test_plot.png")