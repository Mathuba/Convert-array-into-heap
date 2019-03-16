from build_heap import HeapBuilder
import pytest


@pytest.fixture()
def heap_builder(scope='module'):
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
    heap_builder._data.clear()
    heap_builder._data = [1, 2, 3, 4, 5]
    assert heap_builder._data == [1, 2, 3, 4, 5]


def test_generate_old_swap(heap_builder):
    heap_builder._data.clear()
    heap_builder._data = [5, 4, 3, 2, 1]
    heap_builder.generate_swaps()
    assert heap_builder._swaps == [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


def test_generate_old_sorted_heap(heap_builder):
    heap_builder._data.clear()
    heap_builder._data = [1, 2, 3, 4, 5]
    heap_builder.generate_swaps()
    assert heap_builder._swaps == []


# def test_build_heap(heap_builder):
#     heap_builder._data.clear()
#     heap_builder._data = [5, 4, 3, 2, 1]
#     heap_builder.build_heap()
#     assert heap_builder._swaps == [(1, 4), (0, 1), (1, 3)]


def test_build_heap_on_sorted_list(heap_builder):
    heap_builder._data.clear()
    heap_builder._data = [1, 2, 3, 4, 5]
    heap_builder.build_heap()
    assert heap_builder._swaps == []


def test_parent_of_left_child(heap_builder):
    heap_builder._data.clear()
    heap_builder._data = [100, 19, 36, 17, 3, 25, 1, 2, 7]
    left_child_parent = heap_builder.parent(1)
    assert left_child_parent == 0


def test_parent_of_right_child(heap_builder):
    right_child_parent = heap_builder.parent(2)
    assert right_child_parent == 0


def test_parent_of_left_most_leaf(heap_builder):
    left_most_parent_of_child = heap_builder.parent(3)
    assert left_most_parent_of_child == 1


def test_parent_of_right_most_leaf(heap_builder):
    right_most_parent_of_child = heap_builder.parent(4)
    assert right_most_parent_of_child == 1


def test_left_child_of_root(heap_builder):
    left_child = heap_builder.left_child(0)
    assert left_child == 1


def test_left_child_of_uppermost_left_child_node(heap_builder):
    left_child = heap_builder.left_child(1)
    assert left_child == 3


def test_left_child_of_uppermost_right_child_node(heap_builder):
    left_child = heap_builder.left_child(2)
    assert left_child == 5


def test_left_child_of_a_middle_node(heap_builder):
    left_child = heap_builder.left_child(3)
    assert left_child == 7


def test_invalid_left_child(heap_builder):
    left_child = heap_builder.left_child(4)
    node_in_heap = (left_child <= heap_builder._size)
    assert node_in_heap is False


def test_right_child_of_root(heap_builder):
    right_child = heap_builder.right_child(0)
    assert right_child == 2


def test_right_child_of_uppermost_left_child_node(heap_builder):
    right_child = heap_builder.right_child(1)
    assert right_child == 4


def test_right_child_of_uppermost_right_child_node(heap_builder):
    right_child = heap_builder.right_child(2)
    assert right_child == 6


def test_right_child_of_a_middle_node(heap_builder):
    right_child = heap_builder.right_child(3)
    assert right_child == 8


def test_invalid_right_child(heap_builder):
    right_child = heap_builder.right_child(4)
    node_in_heap = (right_child <= heap_builder._size)
    assert node_in_heap is False


def test_sift_down_largest_from_root(heap_builder):
    heap_builder._data.clear()
    heap_builder._swaps.clear()
    heap_builder._data = [50, 30, 15, 19, 20, 10, 5, 2]
    heap_builder.sift_down(0)
    assert heap_builder._data == [15, 30, 5, 19, 20, 10, 50, 2]
    

def test_sift_down_largest_from_uppermost_left_child_node(heap_builder):
    heap_builder._data.clear()
    heap_builder._swaps.clear()
    heap_builder._data = [30, 50, 15, 19, 20, 10, 5, 2]
    heap_builder.sift_down(1)
    assert heap_builder._data == [30, 19, 15, 2, 20, 10, 5, 50]


def test_sift_down_largest_from_uppermost_right_child_node(heap_builder):
    heap_builder._data.clear()
    heap_builder._swaps.clear()
    heap_builder._data = [15, 30, 50, 19, 20, 10, 5, 2]
    heap_builder.sift_down(2)
    assert heap_builder._data == [15, 30, 5, 19, 20, 10, 50, 2]


def test_sift_down_one_place_greater_than_left_child(heap_builder):
    heap_builder._data.clear()
    heap_builder._data = [50, 30, 15, 19, 20, 10, 5, 2]
    heap_builder.sift_down(3)
    assert heap_builder._data == [50, 30, 15, 2, 20, 10, 5, 19]


def test_sift_down_lowest_from_root_node(heap_builder):
    heap_builder._data.clear()
    heap_builder._data = [1, 2, 3, 6, 9, 5, 10, 14]
    heap_builder.sift_down(0)
    assert heap_builder._data == [1, 2, 3, 6, 9, 5, 10, 14]


def test_sift_down_lowest_from_upper_most_left_child_node(heap_builder):
    heap_builder._data.clear()
    heap_builder._data = [2, 1, 3, 6, 9, 5, 10, 14]
    heap_builder.sift_down(1)
    assert heap_builder._data == [2, 1, 3, 6, 9, 5, 10, 14]





