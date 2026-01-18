def sort(arr):
    for i in range(len(arr)):
        min_idx = i

        for k in range(i + 1, len(arr)):
            if arr[k] < arr[min_idx]:
                min_idx = k

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


