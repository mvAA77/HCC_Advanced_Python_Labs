### Tanya Kadiyala
### CMSY-257-300
### Lab 3
### Problem 1: Arrays

class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        self.logicalSize = 0
        for count in range(capacity):
            self.items.append(fill_value)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        if new_item is not None and self.items[index] is None:
            self.logicalSize += 1
        elif new_item is None and self.items[index] is not None:
            self.logicalSize -= 1
        self.items[index] = new_item
    
    def size(self):
        return self.logicalSize

if __name__ == "__main__":
    arr = Array(5)
    arr[0] = 10
    arr[1] = 20
    arr[2] = 30

    print("Logical size:", arr.size())  # expected 3
    print("Physical size:", len(arr))   # expected 5
    print("Array contents:", arr)

    arr[1] = None
    print("Updated logical size:", arr.size())  # expected 2