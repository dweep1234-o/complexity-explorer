def bubble_sort(a):
    a = a[:]                  # work on a copy, don't mutate the input
    ops = 0
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            ops += 1          # one comparison
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                ops += 1      # one swap
                swapped = True
        if not swapped:       # no swaps means the list is sorted
            break
    return a, ops

def insertion_sort(a):
    a = a[:]
    ops = 0
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0:
            ops += 1                  # comparison
            if a[j] <= x:
                break
            a[j + 1] = a[j]           # shift
            ops += 1
            j -= 1
        a[j + 1] = x
    return a, ops


def merge_sort(a):
    a = a[:]
    ops = 0
    buf = [0] * len(a)

    def ms(lo, hi):
        nonlocal ops
        if hi <= lo:
            return
        mid = (lo + hi) // 2
        ms(lo, mid)
        ms(mid + 1, hi)
        i, j, k = lo, mid + 1, lo
        while i <= mid and j <= hi:
            ops += 1                  # comparison
            if a[i] <= a[j]:
                buf[k] = a[i]; i += 1
            else:
                buf[k] = a[j]; j += 1
            k += 1
        while i <= mid:
            buf[k] = a[i]; i += 1; k += 1
        while j <= hi:
            buf[k] = a[j]; j += 1; k += 1
        for t in range(lo, hi + 1):
            a[t] = buf[t]
            ops += 1                  # copy back

    ms(0, len(a) - 1)
    return a, ops


def quicksort(a):
    a = a[:]
    ops = 0
    stack = [(0, len(a) - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue
        # first element as pivot: move it to the end
        a[lo], a[hi] = a[hi], a[lo]
        ops += 1
        pivot = a[hi]
        s = lo
        for i in range(lo, hi):
            ops += 1                  # comparison
            if a[i] < pivot:
                a[i], a[s] = a[s], a[i]
                ops += 1              # swap
                s += 1
        a[s], a[hi] = a[hi], a[s]
        ops += 1
        stack.append((lo, s - 1))
        stack.append((s + 1, hi))
    return a, ops


def heap_sort(a):
    a = a[:]
    ops = 0
    n = len(a)

    def sift(i, end):
        nonlocal ops
        while True:
            left = 2 * i + 1
            if left >= end:
                break
            m = left
            if left + 1 < end:
                ops += 1              # compare the two children
                if a[left + 1] > a[left]:
                    m = left + 1
            ops += 1                  # compare with parent
            if a[m] > a[i]:
                a[i], a[m] = a[m], a[i]
                ops += 1              # swap
                i = m
            else:
                break

    for i in range((n >> 1) - 1, -1, -1):   # build the heap
        sift(i, n)
    for end in range(n - 1, 0, -1):          # move max to the end
        a[0], a[end] = a[end], a[0]
        ops += 1
        sift(0, end)
    return a, ops

def linear_search(a, targets):
    ops = 0
    for t in targets:
        for x in a:
            ops += 1              # one comparison
            if x == t:
                break
    return None, ops / len(targets)


def binary_search(a, targets):
    ops = 0
    for t in targets:
        lo, hi = 0, len(a) - 1
        while lo <= hi:
            ops += 1              # one comparison
            mid = (lo + hi) // 2
            if a[mid] < t:
                lo = mid + 1
            else:
                hi = mid - 1
    return None, ops / len(targets)