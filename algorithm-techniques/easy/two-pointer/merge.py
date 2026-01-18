def merge(num1: list[int], m: int, num2: list[int], n: int )-> None:
    i = m - 1
    k = n - 1
    l = m + n - 1

    while k >= 0:
        if i >= 0 and num1[i] > num2[k]:
            num1[k] = num1[i]

        else:
            num1[i] = num2[k]
            k -= 1
        l -= 1

