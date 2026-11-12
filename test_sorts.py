import random
from algorithms import bubble_sort, insertion_sort, merge_sort, quicksort, heap_sort

for f in (bubble_sort, insertion_sort, merge_sort, quicksort, heap_sort):
    for _ in range(200):
        a = [random.randint(0, 20) for _ in range(random.randint(0, 50))]
        out, _ = f(a)
        assert out == sorted(a), f.__name__
print("all sorts correct")