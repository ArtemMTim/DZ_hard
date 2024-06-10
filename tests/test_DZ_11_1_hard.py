import pytest

from src.DZ_11_1_hard import my_filter, my_map, non_empty_truths, replicate_each

# Тестирование функции non_empty_truths


@pytest.mark.parametrize(
    "list_of_lists, expected",
    [
        ([[0, 1, 2], [], [], [False, True, 42]], [[1, 2], [True, 42]]),
        ([[0, ""], [False, None]], []),
        ([[], []], []),
        ([[0]], []),
    ],
)
def test_non_empty_truths(list_of_lists, expected):
    assert non_empty_truths(list_of_lists) == expected


# Тестирование генераторной функции my_map
def test_my_map():
    def f(x):
        return x * 2

    xs = [0, 1, 2, 3, 4, 5]
    expected_result = [0, 2, 4, 6, 8, 10]
    test_result = my_map(f, xs)
    assert next(test_result) == expected_result[0]
    assert next(test_result) == expected_result[1]
    assert next(test_result) == expected_result[2]
    assert next(test_result) == expected_result[3]
    assert next(test_result) == expected_result[4]


# Тестирование генераторной функции my_filter
def test_my_filter():
    def f(x):
        return x % 2 == 0

    xs = [0, 1, 2, 3, 4, 5]
    expected_result = [0, 2, 4]
    test_result = my_filter(f, xs)
    assert next(test_result) == expected_result[0]
    assert next(test_result) == expected_result[1]
    assert next(test_result) == expected_result[2]


# Тестирование генераторной функции replicate_each
def test_replicate_each():
    n = 3
    xs = [1, "a"]
    expected_result = [1, 1, 1, "a", "a", "a"]
    test_result = replicate_each(n, xs)
    assert next(test_result) == expected_result[0]
    assert next(test_result) == expected_result[1]
    assert next(test_result) == expected_result[2]
    assert next(test_result) == expected_result[3]
    assert next(test_result) == expected_result[4]
    assert next(test_result) == expected_result[5]
