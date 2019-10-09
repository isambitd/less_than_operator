from lessthanop import get_index


def test_with_invalid_input1():
    assert get_index("hello world!!!") == None


def test_with_no_element():
    assert get_index([]) == None


def test_with_only_increasing():
    assert get_index([1, 2, 3, 4, 5]) == 0


def test_with_only_decreasing():
    assert get_index([5, 4, 3, 2, 1]) == 4


def test_with_minimum_at_middle():
    assert get_index([5, 4, 3, 2, 1, 2, 3, 4, 5]) == 4


def test_with_minimum_at_somewhere():
    assert get_index([5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8]) == 4
