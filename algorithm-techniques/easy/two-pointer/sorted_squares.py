def sorted_squares(nums: list) -> list:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    
    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2

        if left_sq > right_sq:
            result[left] = right_sq
            left += 1

        else:
            result[right] = right_sq
            right -= 1
        pos -= 1