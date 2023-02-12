"""
Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.

Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def has_two_numbers(l: [], k: int) -> bool:
    """
    :param l: list of int values
    :param k: integer number
    :return: true whether any two numbers from the list add up to k
    """
    # Create a set from the list `l` to make membership tests faster
    seen = set(l)
    for num in l:
        # Check if the complement of the current element is in the set
        if k - num in seen:
            return True
    # Return False if no two numbers that add up to `k` were found
    return False


if __name__ == "__main__":
    l = [10, 15, 3, 7]
    k = 17
    print(has_two_numbers(l, k))
