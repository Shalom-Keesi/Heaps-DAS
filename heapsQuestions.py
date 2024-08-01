#How do you implement a heap in an array?

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_min(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()  
        self._heapify_down(0)
        return min_value

    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def __str__(self):
        return str(self.heap)

min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(7)
print("Min Heap:", min_heap)
print("Extract Min:", min_heap.extract_min())
print("Min Heap after extraction:", min_heap)





# Implement a heap data structure

class MinHeap:
    def __init__(self):
        self.heap = []
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("extract_min from an empty heap")
        self._swap(0, len(self.heap) - 1)
        min_val = self.heap.pop()
        self._heapify_down(0)
        return min_val
    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2
    def _heapify_down(self, index):
        while (index * 2 + 1) < len(self.heap):
            smallest = index * 2 + 1
            right_child = index * 2 + 2
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child
            if self.heap[index] <= self.heap[smallest]:
                break
            self._swap(index, smallest)
            index = smallest
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(4)
min_heap.insert(15)
min_heap.insert(20)
min_heap.insert(0)
min_heap.insert(8)
print(min_heap.extract_min())
print(min_heap.extract_min())
print(min_heap.extract_min())
min_heap.insert(3)
print(min_heap.extract_min())







# How would you merge k Sorted Lists

import heapq
def merge_k_sorted_lists(lists):
    min_heap = []
    for i, lst in enumerate(lists):
        if lst:  
            heapq.heappush(min_heap, (lst[0], i, 0))
    result = []
    while min_heap:
        val, list_index, element_index = heapq.heappop(min_heap)
        result.append(val)
        if element_index + 1 < len(lists[list_index]):
            next_element = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_element, list_index, element_index + 1))
    return result
lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]
merged_list = merge_k_sorted_lists(lists)
print(merged_list)









# Assuming you are given an array of meeting time intervals consisting of start and end times[start1, end1] ,
#[start2, end2]..., [startN, endN] determine if a person could attend all meetings

def attend(intervals):
    
    intervals.sort(key=lambda x: x[0])  # Sort the intervals by their start times
    for i in range(1, len(intervals)):  # Iterate through the intervals and check for overlaps

        # Checking if the start time of the current meeting is less than the end time of the previous meeting

        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True
intervals = [[0, 30], [5, 10], [15, 20]]
can_attend = attend(intervals)
print(can_attend)
intervals = [[7, 10], [2, 4]]
can_attend = attend(intervals)
print(can_attend)






# Given an array, how would you convert it into a min heap?
def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)
def build_min_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    return arr
