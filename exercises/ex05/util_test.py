"""EX05 - Tests for the utility functions."""
__author__ = "730558895"


from exercises.ex05.utils import only_evens, sub, concat


# Use case
def test_only_evens_sequence() -> None:
    """Test for sequences."""
    list_num: list[int] = [1, 2, 3]
    assert only_evens(list_num) == [2]


# Edge case
def test_only_evens_all_odds() -> None:
    """Test for all odd number lists."""
    list_num: list[int] = [1, 3, 5]
    assert only_evens(list_num) == []


# Use case
def test_only_evens_all_evens() -> None:
    """Test for all even number lists."""
    list_num: list[int] = [4, 4, 4]
    assert only_evens(list_num) == [4, 4, 4]


# Use case
def test_concat_single_number() -> None:
    """Test for single number lists."""
    list_1: list[int] = [1]
    list_2: list[int] = [2]
    assert concat(list_1, list_2) == [1, 2]


# Use case
def test_concat_sequence() -> None:
    """Test for sequences."""
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [4, 5, 6]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6]


# Use case
def test_concat_random_numbers() -> None:
    """Test for random number lists."""
    list_1: list[int] = [1, 1, 0]
    list_2: list[int] = [4, 3, 9, 9]
    assert concat(list_1, list_2) == [1, 1, 0, 4, 3, 9, 9]


# Edge case
def test_concat_empty() -> None:
    """Test for empty lists."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


# Use case
def test_sub_use_sequence() -> None:
    """Test for sequences under use case."""
    input_list: list[int] = [10, 20, 30, 40]
    assert sub(input_list, 1, 3) == [20, 30]


# Use case
def test_sub_use_random() -> None:
    """Test for random number lists under use case."""
    input_list: list[int] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2]
    assert sub(input_list, 5, 14) == [9, 2, 6, 5, 3, 5, 8, 9, 7]


# Edge case
def test_sub_empty() -> None:
    """Test for edge case that would lead to empty list output."""
    input_list: list[int] = [10, 20, 30, 40]
    assert sub(input_list, 100, 0) == []


# Edge case
def test_sub_out_of_scope() -> None:
    """Test for indexes out of scope."""
    input_list: list[int] = [10, 20, 30, 40]
    assert sub(input_list, -1, 100) == [10, 20, 30, 40]