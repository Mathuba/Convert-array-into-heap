# python3


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []
        self._size = 0

    def read_data(self):
        # n = int(input())
        n = 5
        # self._data = [int(s) for s in input().split()]
        self._data = [1, 2, 3, 4, 5]
        assert n == len(self._data)
        self._size = n - 1

    def write_response(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def parent(self, index_i):
        return (index_i - 1) // 2

    def left_child(self, index_i):
        return 2 * index_i + 1

    def right_child(self, index_i):
        return 2 * index_i + 2

    def sift_down(self, index_i):
        self._size = len(self._data)
        min_index = index_i

        left_child_index = self.left_child(index_i)
        if (left_child_index < self._size) and (self._data[left_child_index] < self._data[min_index]):
            min_index = left_child_index

        right_child_index = self.right_child(index_i)
        if (left_child_index < self._size) and (self._data[right_child_index] < self._data[min_index]):
             min_index = right_child_index

        if index_i != min_index:
            self.swap(index_i, min_index)
            self.sift_down(min_index)

    def build_heap(self, an_array):
        size = len(an_array) - 1
        for i in range((len(an_array) // 2), -1, -1):
            self.sift_down(i)

    def swap(self, parent_index, child_index):
        self._swaps.append((parent_index, child_index))
        self._data[parent_index], self._data[child_index] = self._data[child_index], self._data[parent_index]

    def solve(self):
        self.read_data()
        # self.generate_swaps()
        self.build_heap(self._data)
        self.write_response()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.solve()
