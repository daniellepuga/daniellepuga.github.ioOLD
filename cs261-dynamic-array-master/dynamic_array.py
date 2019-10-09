# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME

import numpy as np
class DynamicArray:
    capacity = 10

    def __init__(self):
        self.capacity = 10 #default initial capacity
        self.data = np.ndarray(self.capacity, 'object')
        self.next_index = 0 #initial length of 0

    def is_empty(self):
        if self.next_index > 0:
            return False
        else:
            return True

    def __len__(self):
        return self.next_index

    def append(self, value):
        self.data[self.next_index] = value
        self.add_next_index()
    
    def __getitem__(self, index):
        return self.data[index]

    def add_next_index(self):
        self.next_index += 1

    def clear(self):
        self.next_index = 0

    # def append(self, index):
    #     return 8

    # def darray(self, type):
    #     return type
