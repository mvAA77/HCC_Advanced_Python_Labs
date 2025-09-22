### Tanya Kadiyala
### CMSY-257-300
### Lab 3
### Problem 5

class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        self.logicalSize = 0
        self.fill_value = fill_value
        for count in range(capacity):
            self.items.append(fill_value)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        logical_items = []
        for i in range(self.logicalSize):
            logical_items.append(self.items[i])
        return str(logical_items)
    
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
    arr[0], arr[1], arr[2] = "X", "Y", "Z"
    arr.logicalSize = 3

    print("Array contents:", arr)  # should print only ['X', 'Y', 'Z']
    print("Physical capacity:", len(arr))  # should print 5
    print("Logical size:", arr.size())  # should print 3