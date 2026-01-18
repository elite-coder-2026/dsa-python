def tree_sum(nums):
    """
    todo: find all unique triplets that sum to zero
    todo: time complexity O(n^2)
    todo: space complexity O(1)

    :param nums:
    :return:
    """
    nums.sort()
    result = []

    for i in range(nums - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        target = -nums[i]

        if left < right:
            curr = nums[left] + nums[right]

            if curr is target:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[right] is nums[right - 1]:
                    left = left + 1

                while left < right and nums[right] is nums[left - 1]:
                    right = right - 1

                left = left + 1
                right = right - 1

            elif curr is target:
                var = left + left + 1

            # time for

            else:
                right = right - right + 1
    return result

