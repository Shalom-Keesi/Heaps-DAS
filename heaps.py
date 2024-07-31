class MinHeap:
    def __init__(self):
        self.heap = []  
    #Initializing an empty list to store the heap

    def parent(self, i):
        return (i - 1) // 2  
    #Getting the index of the parent node

    def left_child(self, i):
        return 2 * i + 1  
    #Calculating the index of the left child

    def right_child(self, i):
        return 2 * i + 2  
    # Calculating the index of the right child

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]  
    # Swapping the two elements in the heap

    def insert(self, key):
        self.heap.append(key)  
    # Adding the new element to the end of the heap
        self._heapify_up(len(self.heap) - 1)  

    def _heapify_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent) 
    # Checking if the child is smaller than its parent
            self._heapify_up(parent) 



    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]  
    # Storing the minimum value (root)
        self.heap[0] = self.heap.pop()  
        
        self._heapify_down(0)  
    # Restoring the heap property
        return min_val

    def _heapify_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

     # Comparing root, the left and right child to find the smallest among them
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left

        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        if min_index != i:
            self.swap(i, min_index)
    # Swapping if the root is not the smallest
            self._heapify_down(min_index)  
