# Импортируем необходимые библиотеки
from typing import Callable, Generator, List


def non_empty_truths(list_data: List[list]) -> List[list]:
    """Функция принимает список списков. Возвращает элемента списка, соотсветствующие True"""
    return [[x for x in lst if x] for lst in list_data if [x for x in lst if x]]


def my_map(f: Callable, xs: List) -> Generator:
    """Функция принимает функцию и список. Возвращует значения списка,
    к которым была применена переданная функция."""
    yield from [f(x) for x in xs]


def my_filter(f: Callable, xs: List) -> Generator:
    """Функция принимает функцию и список. Возвращует значения списка, к которым для фильтрации
    была применена переданная функция."""
    yield from [x for x in xs if f(x)]


def replicate_each(n: int, xs: List) -> Generator:
    """Функция принимает значение количества и список. Возвращает значения списка,
    повторяя каждое значение переданное количество раз."""
    for item in xs:
        for _ in range(n):
            yield item
