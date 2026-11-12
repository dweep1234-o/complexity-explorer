import random
import numpy as np
import pandas as pd
import streamlit as st

from algorithms import (bubble_sort, insertion_sort, merge_sort,
                        quicksort, heap_sort, linear_search, binary_search)
from bench import sizes_between, benchmark, fitted_slope, fitted_constant
from inputs import make_input
from plot import plot_results
from theory import predicted_class, GROWTH

SORTS = {"bubble": bubble_sort, "insertion": insertion_sort, "merge": merge_sort,
         "quick": quicksort, "heap": heap_sort}
SEARCHES = {"linear": linear_search, "binary": binary_search}
PATTERNS = ["random", "sorted", "reversed", "nearly", "duplicates"]

st.set_page_config(page_title="Algorithm Complexity Explorer", layout="wide")
st.title("Algorithm Complexity Explorer")
st.caption("Count operations on growing inputs, fit the growth rate, compare it with theory.")

with st.sidebar:
    algo_names = st.multiselect("Algorithms", list(SORTS) + list(SEARCHES),
                                default=["bubble", "insertion", "merge", "quick", "heap"])
    pattern = st.selectbox("Input pattern", PATTERNS)
    max_n = st.slider("Largest n", 500, 8000, 2000, step=500)
    trials = st.slider("Trials per size", 1, 5, 2)
    run = st.button("Run benchmark", type="primary")

if run and algo_names:
    sizes = sizes_between(100, max_n, points=8)
    results, rows = {}, []

    progress = st.progress(0.0, text="Running...")
    for i, name in enumerate(algo_names):
        if name in SORTS:
            ops, _ = benchmark(SORTS[name], pattern, sizes, trials)
        else:
            ops = search_benchmark(SEARCHES[name], pattern, sizes, trials)
        results[name] = ops
        progress.progress((i + 1) / len(algo_names), text=f"Finished {name}")
    progress.empty()

    for name, ops in results.items():
        key = predicted_class(name, pattern)
        f = GROWTH[key]
        rows.append({
            "algorithm": name,
            "predicted": f"O({key})",
                        "predicted slope": round(fitted_slope(sizes, f(np.array(sizes, dtype=float))), 2),
            "measured slope": round(fitted_slope(sizes, ops), 2),
            f"ops at n={sizes[-1]}": round(float(ops[-1]), 1),
        })

    st.pyplot(plot_results(sizes, results, pattern))
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
else:
    st.info("Choose algorithms and a pattern in the sidebar, then press **Run benchmark**.")