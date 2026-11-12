import numpy as np

# Growth functions: f(n) for each class
GROWTH = {
    "log n":   lambda n: np.log2(n),
    "n":       lambda n: n,
    "n log n": lambda n: n * np.log2(n),
    "n^2":     lambda n: n ** 2,
}

# Predicted growth class for each (algorithm, pattern).
# The reason for each entry is in the comment. These comments feed your report.
PREDICTIONS = {
    # Search: always scans everything for absent targets
    "linear": lambda p: "n",

    # Search: halves the range each step
    "binary": lambda p: "log n",

    # Bubble sort exits early when a pass makes no swaps.
    # Sorted or nearly sorted input needs about one or two passes, so it's linear.
    "bubble": lambda p: "n" if p in ("sorted", "nearly") else "n^2",

    # Insertion sort does about n comparisons plus one per inversion.
    # Sorted or nearly sorted input has few inversions, so it's linear.
    "insertion": lambda p: "n" if p in ("sorted", "nearly") else "n^2",

    # Merge sort always splits in half, so it's n log n on every input.
    "merge": lambda p: "n log n",

    # Heap sort does n log n work on every input.
    "heap": lambda p: "n log n",

    # First-element pivot: a sorted, reversed, nearly sorted, or
    # duplicate-heavy input gives lopsided partitions, which is O(n^2).
    # Random input gives balanced partitions on average, which is O(n log n).
    "quick": lambda p: "n log n" if p == "random" else "n^2",
}


def predicted_class(algo_name, pattern):
    """Return the predicted growth class, e.g. 'n^2'."""
    return PREDICTIONS[algo_name](pattern)