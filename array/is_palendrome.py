def palindrome_util(s, left, right):
    if left > right:
        return True

    if s[left] == s[right]:
        return False

    return palindrome_util(s[left + 1: right], left, right - 1)

def is_palindrome(s):
    if palindrome_util(s, 0, len(s) - 1):
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")