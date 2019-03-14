from build_heap import HeapBuilder
import pytest


@pytest.fixture()
def heap_builder():
    """

    :return: HeapBuilder with empty array
    """
    return HeapBuilder()


def test_default(heap_builder):
    assert heap_builder._swaps == []
    assert heap_builder._data == []


def test_unsorted_heap(heap_builder):
    heap_builder._data = [5, 4, 3, 2, 1]
    assert heap_builder._data == [5, 4, 3, 2, 1]


def test_sorted_heap(heap_builder):
    heap_builder._data = [1, 2, 3, 4, 5]
    assert heap_builder._data == [1, 2, 3, 4, 5]


def test_generate_old_swap(heap_builder):
    heap_builder._data = [5, 4, 3, 2, 1]
    heap_builder.generate_swaps()
    assert heap_builder._swaps == [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


def test_generate_old_sorted_heap(heap_builder):
    heap_builder._data = [1, 2, 3, 4, 5]
    heap_builder.generate_swaps()
    assert heap_builder._swaps == []


def test_build_heap(heap_builder):
    heap_builder._data = [5, 4, 3, 2, 1]
    heap_builder.build_heap()
    assert heap_builder._swaps == [(1, 4), (0, 1), (1, 3)]


def test_build_heap_on_sorted_list(heap_builder):
    heap_builder._data = [1, 2, 3, 4, 5]
    heap_builder.build_heap()
    assert heap_builder._swaps == []
