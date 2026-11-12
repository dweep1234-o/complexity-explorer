from theory import predicted_class, GROWTH

for algo in ["bubble", "quick", "merge"]:
    for p in ["random", "sorted"]:
        print(f"{algo:10} {p:8} -> O({predicted_class(algo, p)})")

print(GROWTH["n log n"](1000))