"""EX04 - `list` Utility Functions."""
__author__ = "730558895"


def all(a: list[int], b: int) -> bool:
    """Checking whether an int is found in the list."""
    i: int = 0
    if len(a) == 0:
        return False
    while i < len(a):
        if b != a[i]:
            return False
        i += 1
    return True
    

def max(input: list[int]) -> int:
    """Return the largest integer in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    it: int = 0
    max_number: int = input[it]
    while it + 1 < len(input):
        if max_number < input[it + 1]:
            max_number = input[it + 1]
        it += 1
    return max_number


def is_equal(c: list[int], d: list[int]) -> bool:
    """Checking whether two lists are completely equal."""
    ite: int = 0
    if len(c) == len(d):
        while ite < len(c):
            if c[ite] != d[ite]:
                return False
            ite += 1
        return True
    else:
        return False