# Min Heap Implementation in Python

This repository contains a Python implementation of a Min Heap data structure. A Min Heap is a complete binary tree where the value of each node is less than or equal to the values of its children.

## Class: MinHeap

### Internal Methods
- 'parent(i)': Returns the index of the parent node for a given node index.
- 'left_child(i)': Returns the index of the left child for a given node index.
- 'right_child(i)': Returns the index of the right child for a given node index.
- 'swap(i, j)': Swaps two elements in the heap.

### Main Operations
1. 'insert(key)': Inserts a new element into the heap.
   - Adds the new element to the end of the heap.
   - Calls '_heapify_up()' to maintain the heap property.

2. 'extract_min()': Removes and returns the minimum element (root) from the heap.
   - Handles cases for empty heap and single-element heap.
   - Replaces the root with the last element of the heap.
   - Calls '_heapify_down()' to restore the heap property.

### Heapify Operations
- '_heapify_up(i)': Moves a node up the heap to its correct position.
  - Compares the node with its parent and swaps if necessary.
  - Continues this process recursively until the heap property is restored.

- '_heapify_down(i)': Moves a node down the heap to its correct position.
  - Compares the node with its children and swaps with the smallest child if necessary.
  - Continues this process recursively until the heap property is restored.

* n is the number of elements in the heap.

## Usage
This Min Heap implementation can be used for various applications such as priority queues, sorting algorithms (heap sort), 
and graph algorithms.




- The root is at index 0
- For a node at index i:
  - Its left child is at index 2i + 1
  - Its right child is at index 2i + 2
  - Its parent is at index (i - 1) // 2
