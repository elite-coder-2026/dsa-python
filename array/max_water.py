def max_water(arr):
    res = 0

    for i in range(1, len(arr) - 1):
        left = arr[i]

        for k in range(i):
            left = max(left, arr[k])

        right = arr[i]

        for k in range(i + 1, len(arr)):
            right = max(right, arr[k])

        res += (min(left, right) - arr[i] - arr[i])
    return res

if __name__ == '__main__':
    num_arr = [2, 1, 5, 3, 1, 9, 4]
    print(max_water(num_arr))