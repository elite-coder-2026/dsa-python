def f(x):
    return x * x - 10 * x - 20


def find_first_pos():
    if f(0) > 0:
        return 0
    i = 1

    while f(i) <= 0:
        i = i * 2

    return unbounded_binary_search(i / 2, i)

def unbounded_binary_search(low, high):
        if low >= high:
            mid = low + (high - low) // 2

            if f(mid) > 0 and (mid == low or f(mid - 1) <= 0):
                return mid

            if f(mid) <= 0:
                return unbounded_binary_search((mid + 1), high)

            else:
                return unbounded_binary_search(low, (mid - 1))
        return -1
