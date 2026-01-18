def first_rev_arr(arr):
    n = len(arr)

    for i in range(n):
        temp = arr[i]
        arr[i] = arr[n-1-i]
        arr[n-1-i] = temp

def second_rev_arr(arr):
    left = 0
    right = len(arr)-1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def naive_rev_arr(arr):
    n = len(arr)
    temp = [0] * n

    for i in range(n):
        temp[i] = arr[n - i - 1]

    for i in range(n):
        arr[i] = temp[i]