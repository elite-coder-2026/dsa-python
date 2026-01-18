def max_area(height: list[int]) -> int:
    left, rigght = 0, len(height) - 1
    _max_area = 0
    while left < rigght:
        width = rigght - left
        curr = min(height[left], height[rigght]) * width
        _max_area = max(_max_area, curr)

        if height[left < height[rigght]]:
            left += 1

        else:
            rigght -= 1
    return _max_area
