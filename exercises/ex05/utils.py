"""EX05 - `list` Utility Functions."""
__author__ = "730558895"


def only_evens(input_list: list[int]) -> list[int]:
    """Given a list, return even numbers only."""
    evens: list[int] = list()
    for num in input_list:
        if num % 2 == 0:
            evens.append(num)
    return evens


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Given two lists, return a combination with the first followed by the second."""
    con: list[int] = list_1 + list_2
    return con


def sub(a_list: list[int], in_1: int, in_2: int) -> list[int]:
    """Given a list and two indexes, return a subset of specified start index and the end index - 1."""
    sub_list: list[int] = list()
    i: int = in_1
    if len(a_list) == 0 or in_1 > len(a_list) or in_2 <= 0:
        return sub_list
    if in_1 < 0:
        i: int = 0
    if in_2 > len(a_list) - 1:
        in_2 = len(a_list)
    while in_1 <= i < in_2:
        sub_list.append(a_list[i])
        i += 1
    return sub_list