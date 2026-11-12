import matplotlib
matplotlib.use("Agg")            # draw to a figure without opening a window
import matplotlib.pyplot as plt
import numpy as np
from bench import fitted_constant
from theory import GROWTH, predicted_class


def plot_results(sizes, results, pattern):
    """
    results: dict of algorithm name -> array of mean ops (one value per size)
    Returns a matplotlib Figure.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    sizes_arr = np.asarray(sizes, dtype=float)

    for name, ops in results.items():
        line, = ax.loglog(sizes_arr, ops, "o-", label=f"{name} (measured)")

        key = predicted_class(name, pattern)
        f = GROWTH[key]
        c = fitted_constant(sizes, ops, f)          # scale prediction to match the data
        ax.loglog(sizes_arr, c * f(sizes_arr), "--",
                  color=line.get_color(), label=f"{name} predicted O({key})")

    ax.set_xlabel("input size n")
    ax.set_ylabel("operations")
    ax.set_title(f"Empirical growth vs prediction (pattern: {pattern})")
    ax.legend(fontsize=8)
    ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    return fig